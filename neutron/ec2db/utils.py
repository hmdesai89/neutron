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

def get_paas_ports(context):
    ''' Returns list and detail of ports which belong
        to given paas account. Called from list_port
	api if account in question is a pass account
    '''
    return

def create_pni(context, port_id):
    ''' Add a pni entry in ec2db
    '''
    paas_acc = db_api.get_items(context, "paas")[0]['id']
    LOG.debug('Paas account for pni--')
    LOG.debug(paas_acc)
    db_api.add_item(context,'pni', 
                    { 'os_id' : port_id ,
		      'paas_acc' : paas_acc })
    return


def delete_pni(context, port_id) :
    ''' Remove a pni entry from ec2db
    '''
    LOG.debug('Removing pni--')
    pni = db_api.get_items_ids(context, 'pni', item_os_ids = [port_id])
    LOG.debug(pni)
    db_api.delete_item(context, pni[0][0])
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







