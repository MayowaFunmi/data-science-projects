from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_customer_from_id, get_salesman_from_id, get_chart


def home_view(request):
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        sale_qs = Sale.objects.filter(created__lte=date_to, created__gte=date_from)
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values()) # displays model field names as headings. .values_list() uses numbers as headings
            # get customer name and salesman name instead of their respctive id
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df['updated'] = sales_df['updated'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1, inplace=True)
            # to add another column, eg sales_id column
            #sales_df['sales_id'] = sales_df['id'] .....instead of 'id': 'sales_id' above

            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sales_id': pos.get_sales_id()
                    }
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data)
            # create a new DataFrame out of the two DataFrames
            merged_df = pd.merge(sales_df, positions_df, on='sales_id')
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')

            chart = get_chart(chart_type, df, labels=df['transaction_id'].values)

            # pass DataFrames to html
            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()

        else:
            print('no data')

    context = {
        'form': form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
        'df': df,
        'chart': chart
    }
    return render(request, 'sales/home.html', context)


class SalesListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/main.html'


class SalesDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/detail.html'