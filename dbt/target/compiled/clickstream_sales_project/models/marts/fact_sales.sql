select
  order_id,
  customer_id,
  product_id,
  quantity,
  total_price,
  order_date
from "airflow"."public"."stg_sales"