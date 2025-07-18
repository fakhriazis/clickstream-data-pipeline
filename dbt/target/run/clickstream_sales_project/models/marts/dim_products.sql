
  
    

  create  table "airflow"."public"."dim_products__dbt_tmp"
  
  
    as
  
  (
    with product_data as (
  select distinct
    product_id
  from "airflow"."public"."stg_sales"
)

select
  product_id,
  'Product ' || product_id as product_name
from product_data
  );
  