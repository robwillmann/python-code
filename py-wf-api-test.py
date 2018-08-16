import wavefront_api_client as wave_api
import sys

base_url = 'https://try.wavefront.com'
api_key = sys.argv[1]
config = wave_api.Configuration()
config.host = base_url
client = wave_api.ApiClient(configuration=config, header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate source API
#source_api = wave_api.SourceApi(client)
#sources = source_api.get_all_source()
#print (sources)

id='robs-test-dashboard'
dashboard_api = wave_api.DashboardApi(client)
dashboard = dashboard_api.get_dashboard(id)
print (dashboard)
