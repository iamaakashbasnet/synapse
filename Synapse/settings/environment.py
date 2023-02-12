# ENVIRONMENT = 'prod'
ENVIRONMENT = 'dev'

SETTINGS_MODULE = 'Synapse.settings.dev'

if ENVIRONMENT == 'dev':
    SETTINGS_MODULE = 'Synapse.settings.dev'
if ENVIRONMENT == 'prod':
    SETTINGS_MODULE = 'Synapse.settings.prod'
