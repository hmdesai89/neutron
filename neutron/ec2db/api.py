#    Copyright 2013 Cloudscaling Group, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Defines interface for DB access.

Functions in this module are imported into the ec2api.db namespace. Call these
functions from ec2api.db namespace, not the ec2api.db.api namespace.

**Related Flags**

:dbackend:  string to lookup in the list of LazyPluggable backends.
            `sqlalchemy` is the only supported backend right now.

:connection:  string specifying the sqlalchemy connection to use, like:
              `sqlite:///var/lib/ec2api/ec2api.sqlite`.

"""

from eventlet import tpool
from oslo_config import cfg
from oslo_db import api as db_api


conn = [
    cfg.StrOpt('connection',
                help='ec2 api mysql db location')
]

CONF = cfg.CONF
CONF.register_opts(conn, 'test')

_BACKEND_MAPPING = {'sqlalchemy': 'neutron.ec2db.sqlalchemy.api'}



IMPL = db_api.DBAPI.from_config(cfg.CONF, backend_mapping = _BACKEND_MAPPING )



def add_item(context, kind, data, project_id=None):
    return IMPL.add_item(context, kind, data, project_id=project_id)


def add_item_id(context, kind, os_id, project_id=None):
    return IMPL.add_item_id(context, kind, os_id, project_id=project_id)


def update_item(context, item):
    IMPL.update_item(context, item)


def delete_item(context, item_id):
    IMPL.delete_item(context, item_id)


def restore_item(context, kind, data):
    return IMPL.restore_item(context, kind, data)


def get_items(context, kind):
    return IMPL.get_items(context, kind)


def get_item_by_id(context, item_id):
    return IMPL.get_item_by_id(context, item_id)


def get_items_by_ids(context, item_ids):
    return IMPL.get_items_by_ids(context, item_ids)


def get_public_items(context, kind, item_ids=None):
    return IMPL.get_public_items(context, kind, item_ids)


def get_items_ids(context, kind, item_ids=None, item_os_ids=None):
    return IMPL.get_items_ids(context, kind, item_ids=item_ids,
                              item_os_ids=item_os_ids)


def add_tags(context, tags):
    return IMPL.add_tags(context, tags)


def delete_tags(context, item_ids, tag_pairs=None):
    return IMPL.delete_tags(context, item_ids, tag_pairs)


def get_tags(context, kinds=None, item_ids=None):
    return IMPL.get_tags(context, kinds, item_ids)




if __name__ == '__main__' :
    print 'Starting the test'
