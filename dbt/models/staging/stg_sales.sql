-- staging model: clean and rename raw sales data
with source as (
  select * from {{ source('raw', 'sales_staging') }}
),

renamed as (
  select
    order_id,
    product_id,
    customer_id,
    quantity,
    total_price,
    order_date
  from source
)

select * from renamed
