from oslo_log import log as logging


from neutron.ec2db import api as db_api

LOG = logging.getLogger(__name__)


def is_paas(context, acc_id) :
    '''  Find out whether account in question is 
         paas account or not
    '''
    item = db_api.get_items(context, "paas")
    if item :
        LOG.debug(item)
        return True
    return False

def create_pni(context, port_id):
    ''' Add a pni entry in ec2db
    '''
    paas_acc = db_api.get_items(context, "paas")[0]['id']
    LOG.debug('Paas account for pni--')
    LOG.debug(paas_acc)
    db_api.add_item(context,'pni', 
                    { 'os_data' : port_id ,
		      'paas_acc' : paas_acc })
    return


def delete_pni(context, port_id) :
    ''' Remove a pni entry from ec2db
    '''
    LOG.debug('Removing pni--')
    pnis = db_api.get_items(context, 'pni')
    pni_id = ''    
    for pni in pnis :
        if 'os_data' == port_id :
            pni_id = pni[0]
            break
    LOG.debug(pni_id)
    db_api.delete_item(context, pni_id)
    return



def list_pnis(context) :
    ''' Returns list and detail of ports which belong
        to given paas account. Called from list_port
	api if account in question is a pass account
    '''
    
    LOG.debug("Listing pnis")
    pnis = db_api.get_items(context, 'pni')
    LOG.debug(pnis)
    return pnis







