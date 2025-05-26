import isi_sdk

conn = isi_sdk.Configuration()
conn.host = "10.230.24.249"
conn.verify_ssl = False
conn.username = "root"
conn.password = "p@ncake"

api_client = isi_sdk.ApiClient(conn)

protocol_api = isi_sdk.ProtocolsApi(api_client)

snmp_settings = protocol_api.get_snmp_settings()

print(snmp_settings)

# modify_dict = {}
# modify_dict['system_contact'] = 'aa@aa.cc'
# snmp_settings = isi_sdk.SnmpSettingsExtended(**modify_dict)
# protocol_api.update_snmp_settings(snmp_settings)
