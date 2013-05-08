from django.conf.urls import *

urlpatterns = patterns('staff.views',
    (r'^$', 'todo'),
    (r'^member/$', 'members'),
    (r'^export/$', 'export_members'),
    (r'^bcc/(?P<plan_id>\d+)/$', 'member_bcc'),
    (r'^search/$', 'member_search'),
    (r'^activity/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'activity_date'),
    (r'^activity/today/$', 'activity_today'),
    (r'^activity/$', 'activity'),
    (r'^activity/list/$', 'activity_list'),
    (r'^income/$', 'income'),
    (r'^bill/$', 'bills'),
    (r'^bill/run/$', 'run_billing'),
    (r'^bill/(?P<id>\d+)/$', 'bill'),
    (r'^transaction/$', 'transactions'),
    (r'^transaction/(?P<id>\d+)/$', 'transaction'),
    (r'^stats/$', 'stats'),
    (r'^stats/history/$', 'stats_history'),
    (r'^stats/monthly/$', 'stats_monthly'),
    (r'^stats/gender/$', 'stats_gender'),
    (r'^stats/neighborhood/$', 'stats_neighborhood'),
    (r'^stats/membership-history/$', 'stats_membership_history'),
    (r'^stats/membership-days/$', 'stats_membership_days'),
    (r'^todo/onboard/(?P<id>\d+)/$', 'onboard_task'),
    (r'^todo/exit/(?P<id>\d+)/$', 'exit_task'),
    (r'^deposits/$', 'security_deposits'),
    (r'^signup/$', 'signup'),
    (r'^(?P<member_id>\d+)/$', 'member_detail'),
    (r'^(?P<member_id>\d+)/activity/$', 'member_activity'),
    (r'^(?P<member_id>\d+)/transaction/$', 'member_transactions'),
    (r'^(?P<member_id>\d+)/bill/$', 'member_bills'),
    (r'^(?P<member_id>\d+)/toggle_billing_flag/$', 'toggle_billing_flag'),
    (r'^(?P<member_id>\d+)/membership/$', 'member_membership'),
    (r'^membership/(?P<membership_id>\d+)/$', 'membership'),
    (r'^user_reports/$', 'view_user_reports'),
)

# Copyright 2009 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
