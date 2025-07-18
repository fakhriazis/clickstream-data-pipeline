select
  order_id,
  customer_id,
  product_id,
  quantity,
  total_price,
  order_date
from {{ ref('stg_sales') }}
