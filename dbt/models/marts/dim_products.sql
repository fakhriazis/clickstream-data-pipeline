with product_data as (
  select distinct
    product_id
  from {{ ref('stg_sales') }}
)

select
  product_id,
  'Product ' || product_id as product_name
from product_data
