from fastapi import FastAPI
from src.prediction.api.v1 import biogen
from fastapi_health import health
from src.prediction.api.v1.health_check import healthy_condition, sick_condition
import sentry_sdk
import os 
from dotenv import load_dotenv
import newrelic.agent
from configparser import ConfigParser

# config = ConfigParser()
# config.read('newrelic.ini')

# load_dotenv(r'env/.env')
# url_sentry= os.getenv("sentry_url")
# environment= os.getenv("env")
# app_name= os.getenv("app_name")
# distributed_tracing_enabled= os.getenv("distributed_tracing.enabled")
# transaction_tracer_record_sql= os.getenv("transaction_tracer.record_sql")
# license_key= os.getenv('license_key')

# sentry_sdk.init(url_sentry,
#                 traces_sample_rate=1.0, environment=environment)

# newrelic_app_name= config.get('newrelic', 'app_name')
# newrelic_distributed_tracing_enabled= config.get('newrelic', 'distributed_tracing.enabled')
# newrelic_transaction_tracer_record_sql= config.get('newrelic', 'transaction_tracer.record_sql')
# newrelic_license_key= config.get('newrelic', 'license_key')

# updated_newrelic_app_name= config.set('newrelic', 'app_name', app_name)
# updated_newrelic_distributed_tracing_enabled= config.set('newrelic', 'distributed_tracing.enabled', distributed_tracing_enabled)
# updated_newrelic_transaction_tracer_record_sql= config.set('newrelic', 'transaction_tracer.record_sql', transaction_tracer_record_sql)
# updated_newrelic_license_key= config.set('newrelic', 'license_key', license_key)


# with open('test_update.ini', 'w') as configfile:
#     config.write(configfile)

# newrelic.agent.initialize('test_update.ini')

app = FastAPI()

app.include_router(biogen.predict,tags=["bio_generator"])

app.add_api_route("/health-check", health([healthy_condition, sick_condition]))