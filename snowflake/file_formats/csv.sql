create or replace file format csv type='csv'
    compression = 'auto' field_delimiter = ',' record_delimiter = '\n'
    skip_header = 0 field_optionally_enclosed_by = '\042' trim_space = false
    error_on_column_count_mismatch = false escape = 'none' escape_unenclosed_field = '\134'
    date_format = 'auto' timestamp_format = 'auto' null_if = ('')
    comment = 'file format named csv for ingesting data into snowflake';