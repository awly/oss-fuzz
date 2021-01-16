#!/usr/bin/python3

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

builtin_runtime_yaml="""
plugin_routing:
  connection:
    # test entries
    redirected_local:
      redirect: ansible.builtin.local
    buildah:
      redirect: containers.podman.buildah
    podman:
      redirect: containers.podman.podman
    aws_ssm:
      redirect: community.aws.aws_ssm
    chroot:
      redirect: community.general.chroot
    docker:
      redirect: community.general.docker
    funcd:
      redirect: community.general.funcd
    iocage:
      redirect: community.general.iocage
    jail:
      redirect: community.general.jail
    kubectl:
      redirect: community.kubernetes.kubectl
    libvirt_lxc:
      redirect: community.libvirt.libvirt_lxc
    lxc:
      redirect: community.general.lxc
    lxd:
      redirect: community.general.lxd
    oc:
      redirect: community.general.oc
    qubes:
      redirect: community.general.qubes
    saltstack:
      redirect: community.general.saltstack
    zone:
      redirect: community.general.zone
    vmware_tools:
      redirect: community.vmware.vmware_tools
    httpapi:
      redirect: ansible.netcommon.httpapi
    napalm:
      redirect: ansible.netcommon.napalm
    netconf:
      redirect: ansible.netcommon.netconf
    network_cli:
      redirect: ansible.netcommon.network_cli
    persistent:
      redirect: ansible.netcommon.persistent
  modules:
    # test entry
    formerly_core_ping:
      redirect: testns.testcoll.ping
    # test entry
    uses_redirected_action:
      redirect: ansible.builtin.ping
    podman_container_info:
      redirect: containers.podman.podman_container_info
    podman_image_info:
      redirect: containers.podman.podman_image_info
    podman_image:
      redirect: containers.podman.podman_image
    podman_volume_info:
      redirect: containers.podman.podman_volume_info
    frr_facts:
      redirect: frr.frr.frr_facts
    frr_bgp:
      redirect: frr.frr.frr_bgp
    apt_repo:
      redirect: community.general.apt_repo
    aws_acm_facts:
      redirect: community.aws.aws_acm_facts
    aws_kms_facts:
      redirect: community.aws.aws_kms_facts
    aws_region_facts:
      redirect: community.aws.aws_region_facts
    aws_s3_bucket_facts:
      redirect: community.aws.aws_s3_bucket_facts
    aws_sgw_facts:
      redirect: community.aws.aws_sgw_facts
    aws_waf_facts:
      redirect: community.aws.aws_waf_facts
    cloudfront_facts:
      redirect: community.aws.cloudfront_facts
    cloudwatchlogs_log_group_facts:
      redirect: community.aws.cloudwatchlogs_log_group_facts
    ec2_asg_facts:
      redirect: community.aws.ec2_asg_facts
    ec2_customer_gateway_facts:
      redirect: community.aws.ec2_customer_gateway_facts
    ec2_instance_facts:
      redirect: community.aws.ec2_instance_facts
    ec2_eip_facts:
      redirect: community.aws.ec2_eip_facts
    ec2_elb_facts:
      redirect: community.aws.ec2_elb_facts
    ec2_lc_facts:
      redirect: community.aws.ec2_lc_facts
    ec2_placement_group_facts:
      redirect: community.aws.ec2_placement_group_facts
    ec2_vpc_endpoint_facts:
      redirect: community.aws.ec2_vpc_endpoint_facts
    ec2_vpc_igw_facts:
      redirect: community.aws.ec2_vpc_igw_facts
    ec2_vpc_nacl_facts:
      redirect: community.aws.ec2_vpc_nacl_facts
    ec2_vpc_nat_gateway_facts:
      redirect: community.aws.ec2_vpc_nat_gateway_facts
    ec2_vpc_peering_facts:
      redirect: community.aws.ec2_vpc_peering_facts
    ec2_vpc_route_table_facts:
      redirect: community.aws.ec2_vpc_route_table_facts
    ec2_vpc_vgw_facts:
      redirect: community.aws.ec2_vpc_vgw_facts
    ec2_vpc_vpn_facts:
      redirect: community.aws.ec2_vpc_vpn_facts
    ecs_service_facts:
      redirect: community.aws.ecs_service_facts
    ecs_taskdefinition_facts:
      redirect: community.aws.ecs_taskdefinition_facts
    efs_facts:
      redirect: community.aws.efs_facts
    elasticache_facts:
      redirect: community.aws.elasticache_facts
    elb_application_lb_facts:
      redirect: community.aws.elb_application_lb_facts
    elb_classic_lb_facts:
      redirect: community.aws.elb_classic_lb_facts
    elb_target_facts:
      redirect: community.aws.elb_target_facts
    elb_target_group_facts:
      redirect: community.aws.elb_target_group_facts
    iam_cert_facts:
      redirect: community.aws.iam_cert_facts
    iam_mfa_device_facts:
      redirect: community.aws.iam_mfa_device_facts
    iam_role_facts:
      redirect: community.aws.iam_role_facts
    iam_server_certificate_facts:
      redirect: community.aws.iam_server_certificate_facts
    lambda_facts:
      redirect: community.aws.lambda_facts
    rds_instance_facts:
      redirect: community.aws.rds_instance_facts
    rds_snapshot_facts:
      redirect: community.aws.rds_snapshot_facts
    redshift_facts:
      redirect: community.aws.redshift_facts
    route53_facts:
      redirect: community.aws.route53_facts
    aws_acm:
      redirect: community.aws.aws_acm
    aws_acm_info:
      redirect: community.aws.aws_acm_info
    aws_api_gateway:
      redirect: community.aws.aws_api_gateway
    aws_application_scaling_policy:
      redirect: community.aws.aws_application_scaling_policy
    aws_batch_compute_environment:
      redirect: community.aws.aws_batch_compute_environment
    aws_batch_job_definition:
      redirect: community.aws.aws_batch_job_definition
    aws_batch_job_queue:
      redirect: community.aws.aws_batch_job_queue
    aws_codebuild:
      redirect: community.aws.aws_codebuild
    aws_codecommit:
      redirect: community.aws.aws_codecommit
    aws_codepipeline:
      redirect: community.aws.aws_codepipeline
    aws_config_aggregation_authorization:
      redirect: community.aws.aws_config_aggregation_authorization
    aws_config_aggregator:
      redirect: community.aws.aws_config_aggregator
    aws_config_delivery_channel:
      redirect: community.aws.aws_config_delivery_channel
    aws_config_recorder:
      redirect: community.aws.aws_config_recorder
    aws_config_rule:
      redirect: community.aws.aws_config_rule
    aws_direct_connect_connection:
      redirect: community.aws.aws_direct_connect_connection
    aws_direct_connect_gateway:
      redirect: community.aws.aws_direct_connect_gateway
    aws_direct_connect_link_aggregation_group:
      redirect: community.aws.aws_direct_connect_link_aggregation_group
    aws_direct_connect_virtual_interface:
      redirect: community.aws.aws_direct_connect_virtual_interface
    aws_eks_cluster:
      redirect: community.aws.aws_eks_cluster
    aws_elasticbeanstalk_app:
      redirect: community.aws.aws_elasticbeanstalk_app
    aws_glue_connection:
      redirect: community.aws.aws_glue_connection
    aws_glue_job:
      redirect: community.aws.aws_glue_job
    aws_inspector_target:
      redirect: community.aws.aws_inspector_target
    aws_kms:
      redirect: community.aws.aws_kms
    aws_kms_info:
      redirect: community.aws.aws_kms_info
    aws_region_info:
      redirect: community.aws.aws_region_info
    aws_s3_bucket_info:
      redirect: community.aws.aws_s3_bucket_info
    aws_s3_cors:
      redirect: community.aws.aws_s3_cors
    aws_secret:
      redirect: community.aws.aws_secret
    aws_ses_identity:
      redirect: community.aws.aws_ses_identity
    aws_ses_identity_policy:
      redirect: community.aws.aws_ses_identity_policy
    aws_ses_rule_set:
      redirect: community.aws.aws_ses_rule_set
    aws_sgw_info:
      redirect: community.aws.aws_sgw_info
    aws_ssm_parameter_store:
      redirect: community.aws.aws_ssm_parameter_store
    aws_step_functions_state_machine:
      redirect: community.aws.aws_step_functions_state_machine
    aws_step_functions_state_machine_execution:
      redirect: community.aws.aws_step_functions_state_machine_execution
    aws_waf_condition:
      redirect: community.aws.aws_waf_condition
    aws_waf_info:
      redirect: community.aws.aws_waf_info
    aws_waf_rule:
      redirect: community.aws.aws_waf_rule
    aws_waf_web_acl:
      redirect: community.aws.aws_waf_web_acl
    cloudformation_stack_set:
      redirect: community.aws.cloudformation_stack_set
    cloudformation_exports_info:
      redirect: community.aws.cloudformation_exports_info
    cloudfront_distribution:
      redirect: community.aws.cloudfront_distribution
    cloudfront_info:
      redirect: community.aws.cloudfront_info
    cloudfront_invalidation:
      redirect: community.aws.cloudfront_invalidation
    cloudfront_origin_access_identity:
      redirect: community.aws.cloudfront_origin_access_identity
    cloudtrail:
      redirect: community.aws.cloudtrail
    cloudwatchevent_rule:
      redirect: community.aws.cloudwatchevent_rule
    cloudwatchlogs_log_group:
      redirect: community.aws.cloudwatchlogs_log_group
    cloudwatchlogs_log_group_info:
      redirect: community.aws.cloudwatchlogs_log_group_info
    cloudwatchlogs_log_group_metric_filter:
      redirect: community.aws.cloudwatchlogs_log_group_metric_filter
    data_pipeline:
      redirect: community.aws.data_pipeline
    dms_endpoint:
      redirect: community.aws.dms_endpoint
    dms_replication_subnet_group:
      redirect: community.aws.dms_replication_subnet_group
    dynamodb_table:
      redirect: community.aws.dynamodb_table
    dynamodb_ttl:
      redirect: community.aws.dynamodb_ttl
    ec2_ami_copy:
      redirect: community.aws.ec2_ami_copy
    ec2_asg:
      redirect: community.aws.ec2_asg
    ec2_asg_info:
      redirect: community.aws.ec2_asg_info
    ec2_asg_lifecycle_hook:
      redirect: community.aws.ec2_asg_lifecycle_hook
    ec2_customer_gateway:
      redirect: community.aws.ec2_customer_gateway
    ec2_customer_gateway_info:
      redirect: community.aws.ec2_customer_gateway_info
    ec2_eip:
      redirect: community.aws.ec2_eip
    ec2_eip_info:
      redirect: community.aws.ec2_eip_info
    ec2_elb:
      redirect: community.aws.ec2_elb
    ec2_elb_info:
      redirect: community.aws.ec2_elb_info
    ec2_instance:
      redirect: community.aws.ec2_instance
    ec2_instance_info:
      redirect: community.aws.ec2_instance_info
    ec2_launch_template:
      redirect: community.aws.ec2_launch_template
    ec2_lc:
      redirect: community.aws.ec2_lc
    ec2_lc_find:
      redirect: community.aws.ec2_lc_find
    ec2_lc_info:
      redirect: community.aws.ec2_lc_info
    ec2_metric_alarm:
      redirect: community.aws.ec2_metric_alarm
    ec2_placement_group:
      redirect: community.aws.ec2_placement_group
    ec2_placement_group_info:
      redirect: community.aws.ec2_placement_group_info
    ec2_scaling_policy:
      redirect: community.aws.ec2_scaling_policy
    ec2_snapshot_copy:
      redirect: community.aws.ec2_snapshot_copy
    ec2_transit_gateway:
      redirect: community.aws.ec2_transit_gateway
    ec2_transit_gateway_info:
      redirect: community.aws.ec2_transit_gateway_info
    ec2_vpc_egress_igw:
      redirect: community.aws.ec2_vpc_egress_igw
    ec2_vpc_endpoint:
      redirect: community.aws.ec2_vpc_endpoint
    ec2_vpc_endpoint_info:
      redirect: community.aws.ec2_vpc_endpoint_info
    ec2_vpc_igw:
      redirect: community.aws.ec2_vpc_igw
    ec2_vpc_igw_info:
      redirect: community.aws.ec2_vpc_igw_info
    ec2_vpc_nacl:
      redirect: community.aws.ec2_vpc_nacl
    ec2_vpc_nacl_info:
      redirect: community.aws.ec2_vpc_nacl_info
    ec2_vpc_nat_gateway:
      redirect: community.aws.ec2_vpc_nat_gateway
    ec2_vpc_nat_gateway_info:
      redirect: community.aws.ec2_vpc_nat_gateway_info
    ec2_vpc_peer:
      redirect: community.aws.ec2_vpc_peer
    ec2_vpc_peering_info:
      redirect: community.aws.ec2_vpc_peering_info
    ec2_vpc_route_table:
      redirect: community.aws.ec2_vpc_route_table
    ec2_vpc_route_table_info:
      redirect: community.aws.ec2_vpc_route_table_info
    ec2_vpc_vgw:
      redirect: community.aws.ec2_vpc_vgw
    ec2_vpc_vgw_info:
      redirect: community.aws.ec2_vpc_vgw_info
    ec2_vpc_vpn:
      redirect: community.aws.ec2_vpc_vpn
    ec2_vpc_vpn_info:
      redirect: community.aws.ec2_vpc_vpn_info
    ec2_win_password:
      redirect: community.aws.ec2_win_password
    ecs_attribute:
      redirect: community.aws.ecs_attribute
    ecs_cluster:
      redirect: community.aws.ecs_cluster
    ecs_ecr:
      redirect: community.aws.ecs_ecr
    ecs_service:
      redirect: community.aws.ecs_service
    ecs_service_info:
      redirect: community.aws.ecs_service_info
    ecs_tag:
      redirect: community.aws.ecs_tag
    ecs_task:
      redirect: community.aws.ecs_task
    ecs_taskdefinition:
      redirect: community.aws.ecs_taskdefinition
    ecs_taskdefinition_info:
      redirect: community.aws.ecs_taskdefinition_info
    efs:
      redirect: community.aws.efs
    efs_info:
      redirect: community.aws.efs_info
    elasticache:
      redirect: community.aws.elasticache
    elasticache_info:
      redirect: community.aws.elasticache_info
    elasticache_parameter_group:
      redirect: community.aws.elasticache_parameter_group
    elasticache_snapshot:
      redirect: community.aws.elasticache_snapshot
    elasticache_subnet_group:
      redirect: community.aws.elasticache_subnet_group
    elb_application_lb:
      redirect: community.aws.elb_application_lb
    elb_application_lb_info:
      redirect: community.aws.elb_application_lb_info
    elb_classic_lb:
      redirect: community.aws.elb_classic_lb
    elb_classic_lb_info:
      redirect: community.aws.elb_classic_lb_info
    elb_instance:
      redirect: community.aws.elb_instance
    elb_network_lb:
      redirect: community.aws.elb_network_lb
    elb_target:
      redirect: community.aws.elb_target
    elb_target_group:
      redirect: community.aws.elb_target_group
    elb_target_group_info:
      redirect: community.aws.elb_target_group_info
    elb_target_info:
      redirect: community.aws.elb_target_info
    execute_lambda:
      redirect: community.aws.execute_lambda
    iam:
      redirect: community.aws.iam
    iam_cert:
      redirect: community.aws.iam_cert
    iam_group:
      redirect: community.aws.iam_group
    iam_managed_policy:
      redirect: community.aws.iam_managed_policy
    iam_mfa_device_info:
      redirect: community.aws.iam_mfa_device_info
    iam_password_policy:
      redirect: community.aws.iam_password_policy
    iam_policy:
      redirect: community.aws.iam_policy
    iam_policy_info:
      redirect: community.aws.iam_policy_info
    iam_role:
      redirect: community.aws.iam_role
    iam_role_info:
      redirect: community.aws.iam_role_info
    iam_saml_federation:
      redirect: community.aws.iam_saml_federation
    iam_server_certificate_info:
      redirect: community.aws.iam_server_certificate_info
    iam_user:
      redirect: community.aws.iam_user
    iam_user_info:
      redirect: community.aws.iam_user_info
    kinesis_stream:
      redirect: community.aws.kinesis_stream
    lambda:
      redirect: community.aws.lambda
    lambda_alias:
      redirect: community.aws.lambda_alias
    lambda_event:
      redirect: community.aws.lambda_event
    lambda_info:
      redirect: community.aws.lambda_info
    lambda_policy:
      redirect: community.aws.lambda_policy
    lightsail:
      redirect: community.aws.lightsail
    rds:
      redirect: community.aws.rds
    rds_instance:
      redirect: community.aws.rds_instance
    rds_instance_info:
      redirect: community.aws.rds_instance_info
    rds_param_group:
      redirect: community.aws.rds_param_group
    rds_snapshot:
      redirect: community.aws.rds_snapshot
    rds_snapshot_info:
      redirect: community.aws.rds_snapshot_info
    rds_subnet_group:
      redirect: community.aws.rds_subnet_group
    redshift:
      redirect: community.aws.redshift
    redshift_cross_region_snapshots:
      redirect: community.aws.redshift_cross_region_snapshots
    redshift_info:
      redirect: community.aws.redshift_info
    redshift_subnet_group:
      redirect: community.aws.redshift_subnet_group
    route53:
      redirect: community.aws.route53
    route53_health_check:
      redirect: community.aws.route53_health_check
    route53_info:
      redirect: community.aws.route53_info
    route53_zone:
      redirect: community.aws.route53_zone
    s3_bucket_notification:
      redirect: community.aws.s3_bucket_notification
    s3_lifecycle:
      redirect: community.aws.s3_lifecycle
    s3_logging:
      redirect: community.aws.s3_logging
    s3_sync:
      redirect: community.aws.s3_sync
    s3_website:
      redirect: community.aws.s3_website
    sns:
      redirect: community.aws.sns
    sns_topic:
      redirect: community.aws.sns_topic
    sqs_queue:
      redirect: community.aws.sqs_queue
    sts_assume_role:
      redirect: community.aws.sts_assume_role
    sts_session_token:
      redirect: community.aws.sts_session_token
    ali_instance_facts:
      redirect: community.general.ali_instance_facts
    ali_instance:
      redirect: community.general.ali_instance
    ali_instance_info:
      redirect: community.general.ali_instance_info
    atomic_container:
      redirect: community.general.atomic_container
    atomic_host:
      redirect: community.general.atomic_host
    atomic_image:
      redirect: community.general.atomic_image
    clc_aa_policy:
      redirect: community.general.clc_aa_policy
    clc_alert_policy:
      redirect: community.general.clc_alert_policy
    clc_blueprint_package:
      redirect: community.general.clc_blueprint_package
    clc_firewall_policy:
      redirect: community.general.clc_firewall_policy
    clc_group:
      redirect: community.general.clc_group
    clc_loadbalancer:
      redirect: community.general.clc_loadbalancer
    clc_modify_server:
      redirect: community.general.clc_modify_server
    clc_publicip:
      redirect: community.general.clc_publicip
    clc_server:
      redirect: community.general.clc_server
    clc_server_snapshot:
      redirect: community.general.clc_server_snapshot
    cloudscale_floating_ip:
      redirect: cloudscale_ch.cloud.floating_ip
    cloudscale_server:
      redirect: cloudscale_ch.cloud.server
    cloudscale_server_group:
      redirect: cloudscale_ch.cloud.server_group
    cloudscale_volume:
      redirect: cloudscale_ch.cloud.volume
    cs_instance_facts:
      redirect: ngine_io.cloudstack.cs_instance_info
    cs_zone_facts:
      redirect: ngine_io.cloudstack.cs_zone_info
    cs_account:
      redirect: ngine_io.cloudstack.cs_account
    cs_affinitygroup:
      redirect: ngine_io.cloudstack.cs_affinitygroup
    cs_cluster:
      redirect: ngine_io.cloudstack.cs_cluster
    cs_configuration:
      redirect: ngine_io.cloudstack.cs_configuration
    cs_disk_offering:
      redirect: ngine_io.cloudstack.cs_disk_offering
    cs_domain:
      redirect: ngine_io.cloudstack.cs_domain
    cs_facts:
      redirect: ngine_io.cloudstack.cs_facts
    cs_firewall:
      redirect: ngine_io.cloudstack.cs_firewall
    cs_host:
      redirect: ngine_io.cloudstack.cs_host
    cs_image_store:
      redirect: ngine_io.cloudstack.cs_image_store
    cs_instance:
      redirect: ngine_io.cloudstack.cs_instance
    cs_instance_info:
      redirect: ngine_io.cloudstack.cs_instance_info
    cs_instance_nic:
      redirect: ngine_io.cloudstack.cs_instance_nic
    cs_instance_nic_secondaryip:
      redirect: ngine_io.cloudstack.cs_instance_nic_secondaryip
    cs_instance_password_reset:
      redirect: ngine_io.cloudstack.cs_instance_password_reset
    cs_instancegroup:
      redirect: ngine_io.cloudstack.cs_instancegroup
    cs_ip_address:
      redirect: ngine_io.cloudstack.cs_ip_address
    cs_iso:
      redirect: ngine_io.cloudstack.cs_iso
    cs_loadbalancer_rule:
      redirect: ngine_io.cloudstack.cs_loadbalancer_rule
    cs_loadbalancer_rule_member:
      redirect: ngine_io.cloudstack.cs_loadbalancer_rule_member
    cs_network:
      redirect: ngine_io.cloudstack.cs_network
    cs_network_acl:
      redirect: ngine_io.cloudstack.cs_network_acl
    cs_network_acl_rule:
      redirect: ngine_io.cloudstack.cs_network_acl_rule
    cs_network_offering:
      redirect: ngine_io.cloudstack.cs_network_offering
    cs_physical_network:
      redirect: ngine_io.cloudstack.cs_physical_network
    cs_pod:
      redirect: ngine_io.cloudstack.cs_pod
    cs_portforward:
      redirect: ngine_io.cloudstack.cs_portforward
    cs_project:
      redirect: ngine_io.cloudstack.cs_project
    cs_region:
      redirect: ngine_io.cloudstack.cs_region
    cs_resourcelimit:
      redirect: ngine_io.cloudstack.cs_resourcelimit
    cs_role:
      redirect: ngine_io.cloudstack.cs_role
    cs_role_permission:
      redirect: ngine_io.cloudstack.cs_role_permission
    cs_router:
      redirect: ngine_io.cloudstack.cs_router
    cs_securitygroup:
      redirect: ngine_io.cloudstack.cs_securitygroup
    cs_securitygroup_rule:
      redirect: ngine_io.cloudstack.cs_securitygroup_rule
    cs_service_offering:
      redirect: ngine_io.cloudstack.cs_service_offering
    cs_snapshot_policy:
      redirect: ngine_io.cloudstack.cs_snapshot_policy
    cs_sshkeypair:
      redirect: ngine_io.cloudstack.cs_sshkeypair
    cs_staticnat:
      redirect: ngine_io.cloudstack.cs_staticnat
    cs_storage_pool:
      redirect: ngine_io.cloudstack.cs_storage_pool
    cs_template:
      redirect: ngine_io.cloudstack.cs_template
    cs_traffic_type:
      redirect: ngine_io.cloudstack.cs_traffic_type
    cs_user:
      redirect: ngine_io.cloudstack.cs_user
    cs_vlan_ip_range:
      redirect: ngine_io.cloudstack.cs_vlan_ip_range
    cs_vmsnapshot:
      redirect: ngine_io.cloudstack.cs_vmsnapshot
    cs_volume:
      redirect: ngine_io.cloudstack.cs_volume
    cs_vpc:
      redirect: ngine_io.cloudstack.cs_vpc
    cs_vpc_offering:
      redirect: ngine_io.cloudstack.cs_vpc_offering
    cs_vpn_connection:
      redirect: ngine_io.cloudstack.cs_vpn_connection
    cs_vpn_customer_gateway:
      redirect: ngine_io.cloudstack.cs_vpn_customer_gateway
    cs_vpn_gateway:
      redirect: ngine_io.cloudstack.cs_vpn_gateway
    cs_zone:
      redirect: ngine_io.cloudstack.cs_zone
    cs_zone_info:
      redirect: ngine_io.cloudstack.cs_zone_info
    digital_ocean:
      redirect: community.digitalocean.digital_ocean
    digital_ocean_account_facts:
      redirect: community.digitalocean.digital_ocean_account_facts
    digital_ocean_certificate_facts:
      redirect: community.digitalocean.digital_ocean_certificate_facts
    digital_ocean_domain_facts:
      redirect: community.digitalocean.digital_ocean_domain_facts
    digital_ocean_firewall_facts:
      redirect: community.digitalocean.digital_ocean_firewall_facts
    digital_ocean_floating_ip_facts:
      redirect: community.digitalocean.digital_ocean_floating_ip_facts
    digital_ocean_image_facts:
      redirect: community.digitalocean.digital_ocean_image_facts
    digital_ocean_load_balancer_facts:
      redirect: community.digitalocean.digital_ocean_load_balancer_facts
    digital_ocean_region_facts:
      redirect: community.digitalocean.digital_ocean_region_facts
    digital_ocean_size_facts:
      redirect: community.digitalocean.digital_ocean_size_facts
    digital_ocean_snapshot_facts:
      redirect: community.digitalocean.digital_ocean_snapshot_facts
    digital_ocean_sshkey_facts:
      redirect: community.digitalocean.digital_ocean_sshkey_facts
    digital_ocean_tag_facts:
      redirect: community.digitalocean.digital_ocean_tag_facts
    digital_ocean_volume_facts:
      redirect: community.digitalocean.digital_ocean_volume_facts
    digital_ocean_account_info:
      redirect: community.digitalocean.digital_ocean_account_info
    digital_ocean_block_storage:
      redirect: community.digitalocean.digital_ocean_block_storage
    digital_ocean_certificate:
      redirect: community.digitalocean.digital_ocean_certificate
    digital_ocean_certificate_info:
      redirect: community.digitalocean.digital_ocean_certificate_info
    digital_ocean_domain:
      redirect: community.digitalocean.digital_ocean_domain
    digital_ocean_domain_info:
      redirect: community.digitalocean.digital_ocean_domain_info
    digital_ocean_droplet:
      redirect: community.digitalocean.digital_ocean_droplet
    digital_ocean_firewall_info:
      redirect: community.digitalocean.digital_ocean_firewall_info
    digital_ocean_floating_ip:
      redirect: community.digitalocean.digital_ocean_floating_ip
    digital_ocean_floating_ip_info:
      redirect: community.digitalocean.digital_ocean_floating_ip_info
    digital_ocean_image_info:
      redirect: community.digitalocean.digital_ocean_image_info
    digital_ocean_load_balancer_info:
      redirect: community.digitalocean.digital_ocean_load_balancer_info
    digital_ocean_region_info:
      redirect: community.digitalocean.digital_ocean_region_info
    digital_ocean_size_info:
      redirect: community.digitalocean.digital_ocean_size_info
    digital_ocean_snapshot_info:
      redirect: community.digitalocean.digital_ocean_snapshot_info
    digital_ocean_sshkey:
      redirect: community.digitalocean.digital_ocean_sshkey
    digital_ocean_sshkey_info:
      redirect: community.digitalocean.digital_ocean_sshkey_info
    digital_ocean_tag:
      redirect: community.digitalocean.digital_ocean_tag
    digital_ocean_tag_info:
      redirect: community.digitalocean.digital_ocean_tag_info
    digital_ocean_volume_info:
      redirect: community.digitalocean.digital_ocean_volume_info
    dimensiondata_network:
      redirect: community.general.dimensiondata_network
    dimensiondata_vlan:
      redirect: community.general.dimensiondata_vlan
    docker_image_facts:
      redirect: community.general.docker_image_facts
    docker_service:
      redirect: community.general.docker_service
    docker_compose:
      redirect: community.general.docker_compose
    docker_config:
      redirect: community.general.docker_config
    docker_container:
      redirect: community.general.docker_container
    docker_container_info:
      redirect: community.general.docker_container_info
    docker_host_info:
      redirect: community.general.docker_host_info
    docker_image:
      redirect: community.general.docker_image
    docker_image_info:
      redirect: community.general.docker_image_info
    docker_login:
      redirect: community.general.docker_login
    docker_network:
      redirect: community.general.docker_network
    docker_network_info:
      redirect: community.general.docker_network_info
    docker_node:
      redirect: community.general.docker_node
    docker_node_info:
      redirect: community.general.docker_node_info
    docker_prune:
      redirect: community.general.docker_prune
    docker_secret:
      redirect: community.general.docker_secret
    docker_stack:
      redirect: community.general.docker_stack
    docker_swarm:
      redirect: community.general.docker_swarm
    docker_swarm_info:
      redirect: community.general.docker_swarm_info
    docker_swarm_service:
      redirect: community.general.docker_swarm_service
    docker_swarm_service_info:
      redirect: community.general.docker_swarm_service_info
    docker_volume:
      redirect: community.general.docker_volume
    docker_volume_info:
      redirect: community.general.docker_volume_info
    gcdns_record:
      redirect: community.general.gcdns_record
    gcdns_zone:
      redirect: community.general.gcdns_zone
    gce:
      redirect: community.general.gce
    gcp_backend_service:
      redirect: community.general.gcp_backend_service
    gcp_bigquery_dataset_facts:
      redirect: google.cloud.gcp_bigquery_dataset_info
    gcp_bigquery_table_facts:
      redirect: google.cloud.gcp_bigquery_table_info
    gcp_cloudbuild_trigger_facts:
      redirect: google.cloud.gcp_cloudbuild_trigger_info
    gcp_compute_address_facts:
      redirect: google.cloud.gcp_compute_address_info
    gcp_compute_backend_bucket_facts:
      redirect: google.cloud.gcp_compute_backend_bucket_info
    gcp_compute_backend_service_facts:
      redirect: google.cloud.gcp_compute_backend_service_info
    gcp_compute_disk_facts:
      redirect: google.cloud.gcp_compute_disk_info
    gcp_compute_firewall_facts:
      redirect: google.cloud.gcp_compute_firewall_info
    gcp_compute_forwarding_rule_facts:
      redirect: google.cloud.gcp_compute_forwarding_rule_info
    gcp_compute_global_address_facts:
      redirect: google.cloud.gcp_compute_global_address_info
    gcp_compute_global_forwarding_rule_facts:
      redirect: google.cloud.gcp_compute_global_forwarding_rule_info
    gcp_compute_health_check_facts:
      redirect: google.cloud.gcp_compute_health_check_info
    gcp_compute_http_health_check_facts:
      redirect: google.cloud.gcp_compute_http_health_check_info
    gcp_compute_https_health_check_facts:
      redirect: google.cloud.gcp_compute_https_health_check_info
    gcp_compute_image_facts:
      redirect: google.cloud.gcp_compute_image_info
    gcp_compute_instance_facts:
      redirect: google.cloud.gcp_compute_instance_info
    gcp_compute_instance_group_facts:
      redirect: google.cloud.gcp_compute_instance_group_info
    gcp_compute_instance_group_manager_facts:
      redirect: google.cloud.gcp_compute_instance_group_manager_info
    gcp_compute_instance_template_facts:
      redirect: google.cloud.gcp_compute_instance_template_info
    gcp_compute_interconnect_attachment_facts:
      redirect: google.cloud.gcp_compute_interconnect_attachment_info
    gcp_compute_network_facts:
      redirect: google.cloud.gcp_compute_network_info
    gcp_compute_region_disk_facts:
      redirect: google.cloud.gcp_compute_region_disk_info
    gcp_compute_route_facts:
      redirect: google.cloud.gcp_compute_route_info
    gcp_compute_router_facts:
      redirect: google.cloud.gcp_compute_router_info
    gcp_compute_ssl_certificate_facts:
      redirect: google.cloud.gcp_compute_ssl_certificate_info
    gcp_compute_ssl_policy_facts:
      redirect: google.cloud.gcp_compute_ssl_policy_info
    gcp_compute_subnetwork_facts:
      redirect: google.cloud.gcp_compute_subnetwork_info
    gcp_compute_target_http_proxy_facts:
      redirect: google.cloud.gcp_compute_target_http_proxy_info
    gcp_compute_target_https_proxy_facts:
      redirect: google.cloud.gcp_compute_target_https_proxy_info
    gcp_compute_target_pool_facts:
      redirect: google.cloud.gcp_compute_target_pool_info
    gcp_compute_target_ssl_proxy_facts:
      redirect: google.cloud.gcp_compute_target_ssl_proxy_info
    gcp_compute_target_tcp_proxy_facts:
      redirect: google.cloud.gcp_compute_target_tcp_proxy_info
    gcp_compute_target_vpn_gateway_facts:
      redirect: google.cloud.gcp_compute_target_vpn_gateway_info
    gcp_compute_url_map_facts:
      redirect: google.cloud.gcp_compute_url_map_info
    gcp_compute_vpn_tunnel_facts:
      redirect: google.cloud.gcp_compute_vpn_tunnel_info
    gcp_container_cluster_facts:
      redirect: google.cloud.gcp_container_cluster_info
    gcp_container_node_pool_facts:
      redirect: google.cloud.gcp_container_node_pool_info
    gcp_dns_managed_zone_facts:
      redirect: google.cloud.gcp_dns_managed_zone_info
    gcp_dns_resource_record_set_facts:
      redirect: google.cloud.gcp_dns_resource_record_set_info
    gcp_forwarding_rule:
      redirect: community.general.gcp_forwarding_rule
    gcp_healthcheck:
      redirect: community.general.gcp_healthcheck
    gcp_iam_role_facts:
      redirect: google.cloud.gcp_iam_role_info
    gcp_iam_service_account_facts:
      redirect: google.cloud.gcp_iam_service_account_info
    gcp_pubsub_subscription_facts:
      redirect: google.cloud.gcp_pubsub_subscription_info
    gcp_pubsub_topic_facts:
      redirect: google.cloud.gcp_pubsub_topic_info
    gcp_redis_instance_facts:
      redirect: google.cloud.gcp_redis_instance_info
    gcp_resourcemanager_project_facts:
      redirect: google.cloud.gcp_resourcemanager_project_info
    gcp_sourcerepo_repository_facts:
      redirect: google.cloud.gcp_sourcerepo_repository_info
    gcp_spanner_database_facts:
      redirect: google.cloud.gcp_spanner_database_info
    gcp_spanner_instance_facts:
      redirect: google.cloud.gcp_spanner_instance_info
    gcp_sql_database_facts:
      redirect: google.cloud.gcp_sql_database_info
    gcp_sql_instance_facts:
      redirect: google.cloud.gcp_sql_instance_info
    gcp_sql_user_facts:
      redirect: google.cloud.gcp_sql_user_info
    gcp_target_proxy:
      redirect: community.general.gcp_target_proxy
    gcp_tpu_node_facts:
      redirect: google.cloud.gcp_tpu_node_info
    gcp_url_map:
      redirect: community.general.gcp_url_map
    gcpubsub_facts:
      redirect: community.general.gcpubsub_facts
    gcspanner:
      redirect: community.general.gcspanner
    gc_storage:
      redirect: community.general.gc_storage
    gce_eip:
      redirect: community.general.gce_eip
    gce_img:
      redirect: community.general.gce_img
    gce_instance_template:
      redirect: community.general.gce_instance_template
    gce_labels:
      redirect: community.general.gce_labels
    gce_lb:
      redirect: community.general.gce_lb
    gce_mig:
      redirect: community.general.gce_mig
    gce_net:
      redirect: community.general.gce_net
    gce_pd:
      redirect: community.general.gce_pd
    gce_snapshot:
      redirect: community.general.gce_snapshot
    gce_tag:
      redirect: community.general.gce_tag
    gcpubsub:
      redirect: community.general.gcpubsub
    gcpubsub_info:
      redirect: community.general.gcpubsub_info
    heroku_collaborator:
      redirect: community.general.heroku_collaborator
    hwc_ecs_instance:
      redirect: community.general.hwc_ecs_instance
    hwc_evs_disk:
      redirect: community.general.hwc_evs_disk
    hwc_network_vpc:
      redirect: community.general.hwc_network_vpc
    hwc_smn_topic:
      redirect: community.general.hwc_smn_topic
    hwc_vpc_eip:
      redirect: community.general.hwc_vpc_eip
    hwc_vpc_peering_connect:
      redirect: community.general.hwc_vpc_peering_connect
    hwc_vpc_port:
      redirect: community.general.hwc_vpc_port
    hwc_vpc_private_ip:
      redirect: community.general.hwc_vpc_private_ip
    hwc_vpc_route:
      redirect: community.general.hwc_vpc_route
    hwc_vpc_security_group:
      redirect: community.general.hwc_vpc_security_group
    hwc_vpc_security_group_rule:
      redirect: community.general.hwc_vpc_security_group_rule
    hwc_vpc_subnet:
      redirect: community.general.hwc_vpc_subnet
    kubevirt_cdi_upload:
      redirect: community.general.kubevirt_cdi_upload
    kubevirt_preset:
      redirect: community.general.kubevirt_preset
    kubevirt_pvc:
      redirect: community.general.kubevirt_pvc
    kubevirt_rs:
      redirect: community.general.kubevirt_rs
    kubevirt_template:
      redirect: community.general.kubevirt_template
    kubevirt_vm:
      redirect: community.general.kubevirt_vm
    linode:
      redirect: community.general.linode
    linode_v4:
      redirect: community.general.linode_v4
    lxc_container:
      redirect: community.general.lxc_container
    lxd_container:
      redirect: community.general.lxd_container
    lxd_profile:
      redirect: community.general.lxd_profile
    memset_memstore_facts:
      redirect: community.general.memset_memstore_facts
    memset_server_facts:
      redirect: community.general.memset_server_facts
    memset_dns_reload:
      redirect: community.general.memset_dns_reload
    memset_memstore_info:
      redirect: community.general.memset_memstore_info
    memset_server_info:
      redirect: community.general.memset_server_info
    memset_zone:
      redirect: community.general.memset_zone
    memset_zone_domain:
      redirect: community.general.memset_zone_domain
    memset_zone_record:
      redirect: community.general.memset_zone_record
    cloud_init_data_facts:
      redirect: community.general.cloud_init_data_facts
    helm:
      redirect: community.general.helm
    ovirt:
      redirect: community.general.ovirt
    proxmox:
      redirect: community.general.proxmox
    proxmox_kvm:
      redirect: community.general.proxmox_kvm
    proxmox_template:
      redirect: community.general.proxmox_template
    rhevm:
      redirect: community.general.rhevm
    serverless:
      redirect: community.general.serverless
    terraform:
      redirect: community.general.terraform
    virt:
      redirect: community.libvirt.virt
    virt_net:
      redirect: community.libvirt.virt_net
    virt_pool:
      redirect: community.libvirt.virt_pool
    xenserver_facts:
      redirect: community.general.xenserver_facts
    oneandone_firewall_policy:
      redirect: community.general.oneandone_firewall_policy
    oneandone_load_balancer:
      redirect: community.general.oneandone_load_balancer
    oneandone_monitoring_policy:
      redirect: community.general.oneandone_monitoring_policy
    oneandone_private_network:
      redirect: community.general.oneandone_private_network
    oneandone_public_ip:
      redirect: community.general.oneandone_public_ip
    oneandone_server:
      redirect: community.general.oneandone_server
    online_server_facts:
      redirect: community.general.online_server_facts
    online_user_facts:
      redirect: community.general.online_user_facts
    online_server_info:
      redirect: community.general.online_server_info
    online_user_info:
      redirect: community.general.online_user_info
    one_image_facts:
      redirect: community.general.one_image_facts
    one_host:
      redirect: community.general.one_host
    one_image:
      redirect: community.general.one_image
    one_image_info:
      redirect: community.general.one_image_info
    one_service:
      redirect: community.general.one_service
    one_vm:
      redirect: community.general.one_vm
    os_flavor_facts:
      redirect: openstack.cloud.os_flavor_info
    os_image_facts:
      redirect: openstack.cloud.os_image_info
    os_keystone_domain_facts:
      redirect: openstack.cloud.os_keystone_domain_info
    os_networks_facts:
      redirect: openstack.cloud.os_networks_info
    os_port_facts:
      redirect: openstack.cloud.os_port_info
    os_project_facts:
      redirect: openstack.cloud.os_project_info
    os_server_facts:
      redirect: openstack.cloud.os_server_info
    os_subnets_facts:
      redirect: openstack.cloud.os_subnets_info
    os_user_facts:
      redirect: openstack.cloud.os_user_info
    oci_vcn:
      redirect: community.general.oci_vcn
    ovh_ip_failover:
      redirect: community.general.ovh_ip_failover
    ovh_ip_loadbalancing_backend:
      redirect: community.general.ovh_ip_loadbalancing_backend
    ovh_monthly_billing:
      redirect: community.general.ovh_monthly_billing
    ovirt_affinity_label_facts:
      redirect: community.general.ovirt_affinity_label_facts
    ovirt_api_facts:
      redirect: community.general.ovirt_api_facts
    ovirt_cluster_facts:
      redirect: community.general.ovirt_cluster_facts
    ovirt_datacenter_facts:
      redirect: community.general.ovirt_datacenter_facts
    ovirt_disk_facts:
      redirect: community.general.ovirt_disk_facts
    ovirt_event_facts:
      redirect: community.general.ovirt_event_facts
    ovirt_external_provider_facts:
      redirect: community.general.ovirt_external_provider_facts
    ovirt_group_facts:
      redirect: community.general.ovirt_group_facts
    ovirt_host_facts:
      redirect: community.general.ovirt_host_facts
    ovirt_host_storage_facts:
      redirect: community.general.ovirt_host_storage_facts
    ovirt_network_facts:
      redirect: community.general.ovirt_network_facts
    ovirt_nic_facts:
      redirect: community.general.ovirt_nic_facts
    ovirt_permission_facts:
      redirect: community.general.ovirt_permission_facts
    ovirt_quota_facts:
      redirect: community.general.ovirt_quota_facts
    ovirt_scheduling_policy_facts:
      redirect: community.general.ovirt_scheduling_policy_facts
    ovirt_snapshot_facts:
      redirect: community.general.ovirt_snapshot_facts
    ovirt_storage_domain_facts:
      redirect: community.general.ovirt_storage_domain_facts
    ovirt_storage_template_facts:
      redirect: community.general.ovirt_storage_template_facts
    ovirt_storage_vm_facts:
      redirect: community.general.ovirt_storage_vm_facts
    ovirt_tag_facts:
      redirect: community.general.ovirt_tag_facts
    ovirt_template_facts:
      redirect: community.general.ovirt_template_facts
    ovirt_user_facts:
      redirect: community.general.ovirt_user_facts
    ovirt_vm_facts:
      redirect: community.general.ovirt_vm_facts
    ovirt_vmpool_facts:
      redirect: community.general.ovirt_vmpool_facts
    packet_device:
      redirect: community.general.packet_device
    packet_ip_subnet:
      redirect: community.general.packet_ip_subnet
    packet_project:
      redirect: community.general.packet_project
    packet_sshkey:
      redirect: community.general.packet_sshkey
    packet_volume:
      redirect: community.general.packet_volume
    packet_volume_attachment:
      redirect: community.general.packet_volume_attachment
    profitbricks:
      redirect: community.general.profitbricks
    profitbricks_datacenter:
      redirect: community.general.profitbricks_datacenter
    profitbricks_nic:
      redirect: community.general.profitbricks_nic
    profitbricks_volume:
      redirect: community.general.profitbricks_volume
    profitbricks_volume_attachments:
      redirect: community.general.profitbricks_volume_attachments
    pubnub_blocks:
      redirect: community.general.pubnub_blocks
    rax:
      redirect: community.general.rax
    rax_cbs:
      redirect: community.general.rax_cbs
    rax_cbs_attachments:
      redirect: community.general.rax_cbs_attachments
    rax_cdb:
      redirect: community.general.rax_cdb
    rax_cdb_database:
      redirect: community.general.rax_cdb_database
    rax_cdb_user:
      redirect: community.general.rax_cdb_user
    rax_clb:
      redirect: community.general.rax_clb
    rax_clb_nodes:
      redirect: community.general.rax_clb_nodes
    rax_clb_ssl:
      redirect: community.general.rax_clb_ssl
    rax_dns:
      redirect: community.general.rax_dns
    rax_dns_record:
      redirect: community.general.rax_dns_record
    rax_facts:
      redirect: community.general.rax_facts
    rax_files:
      redirect: community.general.rax_files
    rax_files_objects:
      redirect: community.general.rax_files_objects
    rax_identity:
      redirect: community.general.rax_identity
    rax_keypair:
      redirect: community.general.rax_keypair
    rax_meta:
      redirect: community.general.rax_meta
    rax_mon_alarm:
      redirect: community.general.rax_mon_alarm
    rax_mon_check:
      redirect: community.general.rax_mon_check
    rax_mon_entity:
      redirect: community.general.rax_mon_entity
    rax_mon_notification:
      redirect: community.general.rax_mon_notification
    rax_mon_notification_plan:
      redirect: community.general.rax_mon_notification_plan
    rax_network:
      redirect: community.general.rax_network
    rax_queue:
      redirect: community.general.rax_queue
    rax_scaling_group:
      redirect: community.general.rax_scaling_group
    rax_scaling_policy:
      redirect: community.general.rax_scaling_policy
    scaleway_image_facts:
      redirect: community.general.scaleway_image_facts
    scaleway_ip_facts:
      redirect: community.general.scaleway_ip_facts
    scaleway_organization_facts:
      redirect: community.general.scaleway_organization_facts
    scaleway_security_group_facts:
      redirect: community.general.scaleway_security_group_facts
    scaleway_server_facts:
      redirect: community.general.scaleway_server_facts
    scaleway_snapshot_facts:
      redirect: community.general.scaleway_snapshot_facts
    scaleway_volume_facts:
      redirect: community.general.scaleway_volume_facts
    scaleway_compute:
      redirect: community.general.scaleway_compute
    scaleway_image_info:
      redirect: community.general.scaleway_image_info
    scaleway_ip:
      redirect: community.general.scaleway_ip
    scaleway_ip_info:
      redirect: community.general.scaleway_ip_info
    scaleway_lb:
      redirect: community.general.scaleway_lb
    scaleway_organization_info:
      redirect: community.general.scaleway_organization_info
    scaleway_security_group:
      redirect: community.general.scaleway_security_group
    scaleway_security_group_info:
      redirect: community.general.scaleway_security_group_info
    scaleway_security_group_rule:
      redirect: community.general.scaleway_security_group_rule
    scaleway_server_info:
      redirect: community.general.scaleway_server_info
    scaleway_snapshot_info:
      redirect: community.general.scaleway_snapshot_info
    scaleway_sshkey:
      redirect: community.general.scaleway_sshkey
    scaleway_user_data:
      redirect: community.general.scaleway_user_data
    scaleway_volume:
      redirect: community.general.scaleway_volume
    scaleway_volume_info:
      redirect: community.general.scaleway_volume_info
    smartos_image_facts:
      redirect: community.general.smartos_image_facts
    imgadm:
      redirect: community.general.imgadm
    nictagadm:
      redirect: community.general.nictagadm
    smartos_image_info:
      redirect: community.general.smartos_image_info
    vmadm:
      redirect: community.general.vmadm
    sl_vm:
      redirect: community.general.sl_vm
    spotinst_aws_elastigroup:
      redirect: community.general.spotinst_aws_elastigroup
    udm_dns_record:
      redirect: community.general.udm_dns_record
    udm_dns_zone:
      redirect: community.general.udm_dns_zone
    udm_group:
      redirect: community.general.udm_group
    udm_share:
      redirect: community.general.udm_share
    udm_user:
      redirect: community.general.udm_user
    vr_account_facts:
      redirect: ngine_io.vultr.vultr_account_facts
    vr_dns_domain:
      redirect: ngine_io.vultr.vultr_dns_domain
    vr_dns_record:
      redirect: ngine_io.vultr.vultr_dns_record
    vr_firewall_group:
      redirect: ngine_io.vultr.vultr_firewall_group
    vr_firewall_rule:
      redirect: ngine_io.vultr.vultr_firewall_rule
    vr_server:
      redirect: ngine_io.vultr.vultr_server
    vr_ssh_key:
      redirect: ngine_io.vultr.vultr_ssh_key
    vr_startup_script:
      redirect: ngine_io.vultr.vultr_startup_script
    vr_user:
      redirect: ngine_io.vultr.vultr_user
    vultr_account_facts:
      redirect: ngine_io.vultr.vultr_account_info
    vultr_block_storage_facts:
      redirect: ngine_io.vultr.vultr_block_storage_info
    vultr_dns_domain_facts:
      redirect: ngine_io.vultr.vultr_dns_domain_info
    vultr_firewall_group_facts:
      redirect: ngine_io.vultr.vultr_firewall_group_info
    vultr_network_facts:
      redirect: ngine_io.vultr.vultr_network_info
    vultr_os_facts:
      redirect: ngine_io.vultr.vultr_os_info
    vultr_plan_facts:
      redirect: ngine_io.vultr.vultr_plan_info
    vultr_region_facts:
      redirect: ngine_io.vultr.vultr_region_info
    vultr_server_facts:
      redirect: ngine_io.vultr.vultr_server_info
    vultr_ssh_key_facts:
      redirect: ngine_io.vultr.vultr_ssh_key_info
    vultr_startup_script_facts:
      redirect: ngine_io.vultr.vultr_startup_script_info
    vultr_user_facts:
      redirect: ngine_io.vultr.vultr_user_info
    vultr_account_info:
      redirect: ngine_io.vultr.vultr_account_info
    vultr_block_storage:
      redirect: ngine_io.vultr.vultr_block_storage
    vultr_block_storage_info:
      redirect: ngine_io.vultr.vultr_block_storage_info
    vultr_dns_domain:
      redirect: ngine_io.vultr.vultr_dns_domain
    vultr_dns_domain_info:
      redirect: ngine_io.vultr.vultr_dns_domain_info
    vultr_dns_record:
      redirect: ngine_io.vultr.vultr_dns_record
    vultr_firewall_group:
      redirect: ngine_io.vultr.vultr_firewall_group
    vultr_firewall_group_info:
      redirect: ngine_io.vultr.vultr_firewall_group_info
    vultr_firewall_rule:
      redirect: ngine_io.vultr.vultr_firewall_rule
    vultr_network:
      redirect: ngine_io.vultr.vultr_network
    vultr_network_info:
      redirect: ngine_io.vultr.vultr_network_info
    vultr_os_info:
      redirect: ngine_io.vultr.vultr_os_info
    vultr_plan_info:
      redirect: ngine_io.vultr.vultr_plan_info
    vultr_region_info:
      redirect: ngine_io.vultr.vultr_region_info
    vultr_server:
      redirect: ngine_io.vultr.vultr_server
    vultr_server_info:
      redirect: ngine_io.vultr.vultr_server_info
    vultr_ssh_key:
      redirect: ngine_io.vultr.vultr_ssh_key
    vultr_ssh_key_info:
      redirect: ngine_io.vultr.vultr_ssh_key_info
    vultr_startup_script:
      redirect: ngine_io.vultr.vultr_startup_script
    vultr_startup_script_info:
      redirect: ngine_io.vultr.vultr_startup_script_info
    vultr_user:
      redirect: ngine_io.vultr.vultr_user
    vultr_user_info:
      redirect: ngine_io.vultr.vultr_user_info
    webfaction_app:
      redirect: community.general.webfaction_app
    webfaction_db:
      redirect: community.general.webfaction_db
    webfaction_domain:
      redirect: community.general.webfaction_domain
    webfaction_mailbox:
      redirect: community.general.webfaction_mailbox
    webfaction_site:
      redirect: community.general.webfaction_site
    xenserver_guest_facts:
      redirect: community.general.xenserver_guest_facts
    xenserver_guest:
      redirect: community.general.xenserver_guest
    xenserver_guest_info:
      redirect: community.general.xenserver_guest_info
    xenserver_guest_powerstate:
      redirect: community.general.xenserver_guest_powerstate
    consul:
      redirect: community.general.consul
    consul_acl:
      redirect: community.general.consul_acl
    consul_kv:
      redirect: community.general.consul_kv
    consul_session:
      redirect: community.general.consul_session
    etcd3:
      redirect: community.general.etcd3
    pacemaker_cluster:
      redirect: community.general.pacemaker_cluster
    znode:
      redirect: community.general.znode
    aerospike_migrations:
      redirect: community.general.aerospike_migrations
    influxdb_database:
      redirect: community.general.influxdb_database
    influxdb_query:
      redirect: community.general.influxdb_query
    influxdb_retention_policy:
      redirect: community.general.influxdb_retention_policy
    influxdb_user:
      redirect: community.general.influxdb_user
    influxdb_write:
      redirect: community.general.influxdb_write
    elasticsearch_plugin:
      redirect: community.general.elasticsearch_plugin
    kibana_plugin:
      redirect: community.general.kibana_plugin
    redis:
      redirect: community.general.redis
    riak:
      redirect: community.general.riak
    mssql_db:
      redirect: community.general.mssql_db
    mysql_db:
      redirect: community.mysql.mysql_db
    mysql_info:
      redirect: community.mysql.mysql_info
    mysql_query:
      redirect: community.mysql.mysql_query
    mysql_replication:
      redirect: community.mysql.mysql_replication
    mysql_user:
      redirect: community.mysql.mysql_user
    mysql_variables:
      redirect: community.mysql.mysql_variables
    postgresql_copy:
      redirect: community.general.postgresql_copy
    postgresql_db:
      redirect: community.general.postgresql_db
    postgresql_ext:
      redirect: community.general.postgresql_ext
    postgresql_idx:
      redirect: community.general.postgresql_idx
    postgresql_info:
      redirect: community.general.postgresql_info
    postgresql_lang:
      redirect: community.general.postgresql_lang
    postgresql_membership:
      redirect: community.general.postgresql_membership
    postgresql_owner:
      redirect: community.general.postgresql_owner
    postgresql_pg_hba:
      redirect: community.general.postgresql_pg_hba
    postgresql_ping:
      redirect: community.general.postgresql_ping
    postgresql_privs:
      redirect: community.general.postgresql_privs
    postgresql_publication:
      redirect: community.general.postgresql_publication
    postgresql_query:
      redirect: community.general.postgresql_query
    postgresql_schema:
      redirect: community.general.postgresql_schema
    postgresql_sequence:
      redirect: community.general.postgresql_sequence
    postgresql_set:
      redirect: community.general.postgresql_set
    postgresql_slot:
      redirect: community.general.postgresql_slot
    postgresql_subscription:
      redirect: community.general.postgresql_subscription
    postgresql_table:
      redirect: community.general.postgresql_table
    postgresql_tablespace:
      redirect: community.general.postgresql_tablespace
    postgresql_user:
      redirect: community.general.postgresql_user
    postgresql_user_obj_stat_info:
      redirect: community.general.postgresql_user_obj_stat_info
    proxysql_backend_servers:
      redirect: community.proxysql.proxysql_backend_servers
    proxysql_global_variables:
      redirect: community.proxysql.proxysql_global_variables
    proxysql_manage_config:
      redirect: community.proxysql.proxysql_manage_config
    proxysql_mysql_users:
      redirect: community.proxysql.proxysql_mysql_users
    proxysql_query_rules:
      redirect: community.proxysql.proxysql_query_rules
    proxysql_replication_hostgroups:
      redirect: community.proxysql.proxysql_replication_hostgroups
    proxysql_scheduler:
      redirect: community.proxysql.proxysql_scheduler
    vertica_facts:
      redirect: community.general.vertica_facts
    vertica_configuration:
      redirect: community.general.vertica_configuration
    vertica_info:
      redirect: community.general.vertica_info
    vertica_role:
      redirect: community.general.vertica_role
    vertica_schema:
      redirect: community.general.vertica_schema
    vertica_user:
      redirect: community.general.vertica_user
    archive:
      redirect: community.general.archive
    ini_file:
      redirect: community.general.ini_file
    iso_extract:
      redirect: community.general.iso_extract
    patch:
      redirect: ansible.posix.patch
    read_csv:
      redirect: community.general.read_csv
    xattr:
      redirect: community.general.xattr
    xml:
      redirect: community.general.xml
    onepassword_facts:
      redirect: community.general.onepassword_facts
    ipa_config:
      redirect: community.general.ipa_config
    ipa_dnsrecord:
      redirect: community.general.ipa_dnsrecord
    ipa_dnszone:
      redirect: community.general.ipa_dnszone
    ipa_group:
      redirect: community.general.ipa_group
    ipa_hbacrule:
      redirect: community.general.ipa_hbacrule
    ipa_host:
      redirect: community.general.ipa_host
    ipa_hostgroup:
      redirect: community.general.ipa_hostgroup
    ipa_role:
      redirect: community.general.ipa_role
    ipa_service:
      redirect: community.general.ipa_service
    ipa_subca:
      redirect: community.general.ipa_subca
    ipa_sudocmd:
      redirect: community.general.ipa_sudocmd
    ipa_sudocmdgroup:
      redirect: community.general.ipa_sudocmdgroup
    ipa_sudorule:
      redirect: community.general.ipa_sudorule
    ipa_user:
      redirect: community.general.ipa_user
    ipa_vault:
      redirect: community.general.ipa_vault
    keycloak_client:
      redirect: community.general.keycloak_client
    keycloak_clienttemplate:
      redirect: community.general.keycloak_clienttemplate
    keycloak_group:
      redirect: community.general.keycloak_group
    onepassword_info:
      redirect: community.general.onepassword_info
    opendj_backendprop:
      redirect: community.general.opendj_backendprop
    rabbitmq_binding:
      redirect: community.rabbitmq.rabbitmq_binding
    rabbitmq_exchange:
      redirect: community.rabbitmq.rabbitmq_exchange
    rabbitmq_global_parameter:
      redirect: community.rabbitmq.rabbitmq_global_parameter
    rabbitmq_parameter:
      redirect: community.rabbitmq.rabbitmq_parameter
    rabbitmq_plugin:
      redirect: community.rabbitmq.rabbitmq_plugin
    rabbitmq_policy:
      redirect: community.rabbitmq.rabbitmq_policy
    rabbitmq_queue:
      redirect: community.rabbitmq.rabbitmq_queue
    rabbitmq_user:
      redirect: community.rabbitmq.rabbitmq_user
    rabbitmq_vhost:
      redirect: community.rabbitmq.rabbitmq_vhost
    rabbitmq_vhost_limits:
      redirect: community.rabbitmq.rabbitmq_vhost_limits
    airbrake_deployment:
      redirect: community.general.airbrake_deployment
    bigpanda:
      redirect: community.general.bigpanda
    circonus_annotation:
      redirect: community.general.circonus_annotation
    datadog_event:
      redirect: community.general.datadog_event
    datadog_monitor:
      redirect: community.general.datadog_monitor
    honeybadger_deployment:
      redirect: community.general.honeybadger_deployment
    icinga2_feature:
      redirect: community.general.icinga2_feature
    icinga2_host:
      redirect: community.general.icinga2_host
    librato_annotation:
      redirect: community.general.librato_annotation
    logentries:
      redirect: community.general.logentries
    logicmonitor:
      redirect: community.general.logicmonitor
    logicmonitor_facts:
      redirect: community.general.logicmonitor_facts
    logstash_plugin:
      redirect: community.general.logstash_plugin
    monit:
      redirect: community.general.monit
    nagios:
      redirect: community.general.nagios
    newrelic_deployment:
      redirect: community.general.newrelic_deployment
    pagerduty:
      redirect: community.general.pagerduty
    pagerduty_alert:
      redirect: community.general.pagerduty_alert
    pingdom:
      redirect: community.general.pingdom
    rollbar_deployment:
      redirect: community.general.rollbar_deployment
    sensu_check:
      redirect: community.general.sensu_check
    sensu_client:
      redirect: community.general.sensu_client
    sensu_handler:
      redirect: community.general.sensu_handler
    sensu_silence:
      redirect: community.general.sensu_silence
    sensu_subscription:
      redirect: community.general.sensu_subscription
    spectrum_device:
      redirect: community.general.spectrum_device
    stackdriver:
      redirect: community.general.stackdriver
    statusio_maintenance:
      redirect: community.general.statusio_maintenance
    uptimerobot:
      redirect: community.general.uptimerobot
    zabbix_group_facts:
      redirect: community.zabbix.zabbix_group_facts
    zabbix_host_facts:
      redirect: community.zabbix.zabbix_host_facts
    zabbix_action:
      redirect: community.zabbix.zabbix_action
    zabbix_group:
      redirect: community.zabbix.zabbix_group
    zabbix_group_info:
      redirect: community.zabbix.zabbix_group_info
    zabbix_host:
      redirect: community.zabbix.zabbix_host
    zabbix_host_events_info:
      redirect: community.zabbix.zabbix_host_events_info
    zabbix_host_info:
      redirect: community.zabbix.zabbix_host_info
    zabbix_hostmacro:
      redirect: community.zabbix.zabbix_hostmacro
    zabbix_maintenance:
      redirect: community.zabbix.zabbix_maintenance
    zabbix_map:
      redirect: community.zabbix.zabbix_map
    zabbix_mediatype:
      redirect: community.zabbix.zabbix_mediatype
    zabbix_proxy:
      redirect: community.zabbix.zabbix_proxy
    zabbix_screen:
      redirect: community.zabbix.zabbix_screen
    zabbix_service:
      redirect: community.zabbix.zabbix_service
    zabbix_template:
      redirect: community.zabbix.zabbix_template
    zabbix_template_info:
      redirect: community.zabbix.zabbix_template_info
    zabbix_user:
      redirect: community.zabbix.zabbix_user
    zabbix_user_info:
      redirect: community.zabbix.zabbix_user_info
    zabbix_valuemap:
      redirect: community.zabbix.zabbix_valuemap
    cloudflare_dns:
      redirect: community.general.cloudflare_dns
    dnsimple:
      redirect: community.general.dnsimple
    dnsmadeeasy:
      redirect: community.general.dnsmadeeasy
    exo_dns_domain:
      redirect: ngine_io.exoscale.exo_dns_domain
    exo_dns_record:
      redirect: ngine_io.exoscale.exo_dns_record
    haproxy:
      redirect: community.general.haproxy
    hetzner_failover_ip:
      redirect: community.general.hetzner_failover_ip
    hetzner_failover_ip_info:
      redirect: community.general.hetzner_failover_ip_info
    hetzner_firewall:
      redirect: community.general.hetzner_firewall
    hetzner_firewall_info:
      redirect: community.general.hetzner_firewall_info
    infinity:
      redirect: community.general.infinity
    ip_netns:
      redirect: community.general.ip_netns
    ipify_facts:
      redirect: community.general.ipify_facts
    ipinfoio_facts:
      redirect: community.general.ipinfoio_facts
    ipwcli_dns:
      redirect: community.general.ipwcli_dns
    ldap_attr:
      redirect: community.general.ldap_attr
    ldap_attrs:
      redirect: community.general.ldap_attrs
    ldap_entry:
      redirect: community.general.ldap_entry
    ldap_passwd:
      redirect: community.general.ldap_passwd
    lldp:
      redirect: community.general.lldp
    netcup_dns:
      redirect: community.general.netcup_dns
    nios_a_record:
      redirect: community.general.nios_a_record
    nios_aaaa_record:
      redirect: community.general.nios_aaaa_record
    nios_cname_record:
      redirect: community.general.nios_cname_record
    nios_dns_view:
      redirect: community.general.nios_dns_view
    nios_fixed_address:
      redirect: community.general.nios_fixed_address
    nios_host_record:
      redirect: community.general.nios_host_record
    nios_member:
      redirect: community.general.nios_member
    nios_mx_record:
      redirect: community.general.nios_mx_record
    nios_naptr_record:
      redirect: community.general.nios_naptr_record
    nios_network:
      redirect: community.general.nios_network
    nios_network_view:
      redirect: community.general.nios_network_view
    nios_nsgroup:
      redirect: community.general.nios_nsgroup
    nios_ptr_record:
      redirect: community.general.nios_ptr_record
    nios_srv_record:
      redirect: community.general.nios_srv_record
    nios_txt_record:
      redirect: community.general.nios_txt_record
    nios_zone:
      redirect: community.general.nios_zone
    nmcli:
      redirect: community.general.nmcli
    nsupdate:
      redirect: community.general.nsupdate
    omapi_host:
      redirect: community.general.omapi_host
    snmp_facts:
      redirect: community.general.snmp_facts
    a10_server:
      redirect: community.network.a10_server
    a10_server_axapi3:
      redirect: community.network.a10_server_axapi3
    a10_service_group:
      redirect: community.network.a10_service_group
    a10_virtual_server:
      redirect: community.network.a10_virtual_server
    aci_intf_policy_fc:
      redirect: cisco.aci.aci_interface_policy_fc
    aci_intf_policy_l2:
      redirect: cisco.aci.aci_interface_policy_l2
    aci_intf_policy_lldp:
      redirect: cisco.aci.aci_interface_policy_lldp
    aci_intf_policy_mcp:
      redirect: cisco.aci.aci_interface_policy_mcp
    aci_intf_policy_port_channel:
      redirect: cisco.aci.aci_interface_policy_port_channel
    aci_intf_policy_port_security:
      redirect: cisco.aci.aci_interface_policy_port_security
    mso_schema_template_external_epg_contract:
      redirect: cisco.mso.mso_schema_template_external_epg_contract
    mso_schema_template_external_epg_subnet:
      redirect: cisco.mso.mso_schema_template_external_epg_subnet
    aireos_command:
      redirect: community.network.aireos_command
    aireos_config:
      redirect: community.network.aireos_config
    apconos_command:
      redirect: community.network.apconos_command
    aruba_command:
      redirect: community.network.aruba_command
    aruba_config:
      redirect: community.network.aruba_config
    avi_actiongroupconfig:
      redirect: community.network.avi_actiongroupconfig
    avi_alertconfig:
      redirect: community.network.avi_alertconfig
    avi_alertemailconfig:
      redirect: community.network.avi_alertemailconfig
    avi_alertscriptconfig:
      redirect: community.network.avi_alertscriptconfig
    avi_alertsyslogconfig:
      redirect: community.network.avi_alertsyslogconfig
    avi_analyticsprofile:
      redirect: community.network.avi_analyticsprofile
    avi_api_session:
      redirect: community.network.avi_api_session
    avi_api_version:
      redirect: community.network.avi_api_version
    avi_applicationpersistenceprofile:
      redirect: community.network.avi_applicationpersistenceprofile
    avi_applicationprofile:
      redirect: community.network.avi_applicationprofile
    avi_authprofile:
      redirect: community.network.avi_authprofile
    avi_autoscalelaunchconfig:
      redirect: community.network.avi_autoscalelaunchconfig
    avi_backup:
      redirect: community.network.avi_backup
    avi_backupconfiguration:
      redirect: community.network.avi_backupconfiguration
    avi_certificatemanagementprofile:
      redirect: community.network.avi_certificatemanagementprofile
    avi_cloud:
      redirect: community.network.avi_cloud
    avi_cloudconnectoruser:
      redirect: community.network.avi_cloudconnectoruser
    avi_cloudproperties:
      redirect: community.network.avi_cloudproperties
    avi_cluster:
      redirect: community.network.avi_cluster
    avi_clusterclouddetails:
      redirect: community.network.avi_clusterclouddetails
    avi_controllerproperties:
      redirect: community.network.avi_controllerproperties
    avi_customipamdnsprofile:
      redirect: community.network.avi_customipamdnsprofile
    avi_dnspolicy:
      redirect: community.network.avi_dnspolicy
    avi_errorpagebody:
      redirect: community.network.avi_errorpagebody
    avi_errorpageprofile:
      redirect: community.network.avi_errorpageprofile
    avi_gslb:
      redirect: community.network.avi_gslb
    avi_gslbgeodbprofile:
      redirect: community.network.avi_gslbgeodbprofile
    avi_gslbservice:
      redirect: community.network.avi_gslbservice
    avi_gslbservice_patch_member:
      redirect: community.network.avi_gslbservice_patch_member
    avi_hardwaresecuritymodulegroup:
      redirect: community.network.avi_hardwaresecuritymodulegroup
    avi_healthmonitor:
      redirect: community.network.avi_healthmonitor
    avi_httppolicyset:
      redirect: community.network.avi_httppolicyset
    avi_ipaddrgroup:
      redirect: community.network.avi_ipaddrgroup
    avi_ipamdnsproviderprofile:
      redirect: community.network.avi_ipamdnsproviderprofile
    avi_l4policyset:
      redirect: community.network.avi_l4policyset
    avi_microservicegroup:
      redirect: community.network.avi_microservicegroup
    avi_network:
      redirect: community.network.avi_network
    avi_networkprofile:
      redirect: community.network.avi_networkprofile
    avi_networksecuritypolicy:
      redirect: community.network.avi_networksecuritypolicy
    avi_pkiprofile:
      redirect: community.network.avi_pkiprofile
    avi_pool:
      redirect: community.network.avi_pool
    avi_poolgroup:
      redirect: community.network.avi_poolgroup
    avi_poolgroupdeploymentpolicy:
      redirect: community.network.avi_poolgroupdeploymentpolicy
    avi_prioritylabels:
      redirect: community.network.avi_prioritylabels
    avi_role:
      redirect: community.network.avi_role
    avi_scheduler:
      redirect: community.network.avi_scheduler
    avi_seproperties:
      redirect: community.network.avi_seproperties
    avi_serverautoscalepolicy:
      redirect: community.network.avi_serverautoscalepolicy
    avi_serviceengine:
      redirect: community.network.avi_serviceengine
    avi_serviceenginegroup:
      redirect: community.network.avi_serviceenginegroup
    avi_snmptrapprofile:
      redirect: community.network.avi_snmptrapprofile
    avi_sslkeyandcertificate:
      redirect: community.network.avi_sslkeyandcertificate
    avi_sslprofile:
      redirect: community.network.avi_sslprofile
    avi_stringgroup:
      redirect: community.network.avi_stringgroup
    avi_systemconfiguration:
      redirect: community.network.avi_systemconfiguration
    avi_tenant:
      redirect: community.network.avi_tenant
    avi_trafficcloneprofile:
      redirect: community.network.avi_trafficcloneprofile
    avi_user:
      redirect: community.network.avi_user
    avi_useraccount:
      redirect: community.network.avi_useraccount
    avi_useraccountprofile:
      redirect: community.network.avi_useraccountprofile
    avi_virtualservice:
      redirect: community.network.avi_virtualservice
    avi_vrfcontext:
      redirect: community.network.avi_vrfcontext
    avi_vsdatascriptset:
      redirect: community.network.avi_vsdatascriptset
    avi_vsvip:
      redirect: community.network.avi_vsvip
    avi_webhook:
      redirect: community.network.avi_webhook
    bcf_switch:
      redirect: community.network.bcf_switch
    bigmon_chain:
      redirect: community.network.bigmon_chain
    bigmon_policy:
      redirect: community.network.bigmon_policy
    checkpoint_access_layer_facts:
      redirect: check_point.mgmt.checkpoint_access_layer_facts
    checkpoint_access_rule:
      redirect: check_point.mgmt.checkpoint_access_rule
    checkpoint_access_rule_facts:
      redirect: check_point.mgmt.checkpoint_access_rule_facts
    checkpoint_host:
      redirect: check_point.mgmt.checkpoint_host
    checkpoint_host_facts:
      redirect: check_point.mgmt.checkpoint_host_facts
    checkpoint_object_facts:
      redirect: check_point.mgmt.checkpoint_object_facts
    checkpoint_run_script:
      redirect: check_point.mgmt.checkpoint_run_script
    checkpoint_session:
      redirect: check_point.mgmt.checkpoint_session
    checkpoint_task_facts:
      redirect: check_point.mgmt.checkpoint_task_facts
    cp_publish:
      redirect: community.network.cp_publish
    ce_aaa_server:
      redirect: community.network.ce_aaa_server
    ce_aaa_server_host:
      redirect: community.network.ce_aaa_server_host
    ce_acl:
      redirect: community.network.ce_acl
    ce_acl_advance:
      redirect: community.network.ce_acl_advance
    ce_acl_interface:
      redirect: community.network.ce_acl_interface
    ce_bfd_global:
      redirect: community.network.ce_bfd_global
    ce_bfd_session:
      redirect: community.network.ce_bfd_session
    ce_bfd_view:
      redirect: community.network.ce_bfd_view
    ce_bgp:
      redirect: community.network.ce_bgp
    ce_bgp_af:
      redirect: community.network.ce_bgp_af
    ce_bgp_neighbor:
      redirect: community.network.ce_bgp_neighbor
    ce_bgp_neighbor_af:
      redirect: community.network.ce_bgp_neighbor_af
    ce_command:
      redirect: community.network.ce_command
    ce_config:
      redirect: community.network.ce_config
    ce_dldp:
      redirect: community.network.ce_dldp
    ce_dldp_interface:
      redirect: community.network.ce_dldp_interface
    ce_eth_trunk:
      redirect: community.network.ce_eth_trunk
    ce_evpn_bd_vni:
      redirect: community.network.ce_evpn_bd_vni
    ce_evpn_bgp:
      redirect: community.network.ce_evpn_bgp
    ce_evpn_bgp_rr:
      redirect: community.network.ce_evpn_bgp_rr
    ce_evpn_global:
      redirect: community.network.ce_evpn_global
    ce_facts:
      redirect: community.network.ce_facts
    ce_file_copy:
      redirect: community.network.ce_file_copy
    ce_info_center_debug:
      redirect: community.network.ce_info_center_debug
    ce_info_center_global:
      redirect: community.network.ce_info_center_global
    ce_info_center_log:
      redirect: community.network.ce_info_center_log
    ce_info_center_trap:
      redirect: community.network.ce_info_center_trap
    ce_interface:
      redirect: community.network.ce_interface
    ce_interface_ospf:
      redirect: community.network.ce_interface_ospf
    ce_ip_interface:
      redirect: community.network.ce_ip_interface
    ce_is_is_instance:
      redirect: community.network.ce_is_is_instance
    ce_is_is_interface:
      redirect: community.network.ce_is_is_interface
    ce_is_is_view:
      redirect: community.network.ce_is_is_view
    ce_lacp:
      redirect: community.network.ce_lacp
    ce_link_status:
      redirect: community.network.ce_link_status
    ce_lldp:
      redirect: community.network.ce_lldp
    ce_lldp_interface:
      redirect: community.network.ce_lldp_interface
    ce_mdn_interface:
      redirect: community.network.ce_mdn_interface
    ce_mlag_config:
      redirect: community.network.ce_mlag_config
    ce_mlag_interface:
      redirect: community.network.ce_mlag_interface
    ce_mtu:
      redirect: community.network.ce_mtu
    ce_multicast_global:
      redirect: community.network.ce_multicast_global
    ce_multicast_igmp_enable:
      redirect: community.network.ce_multicast_igmp_enable
    ce_netconf:
      redirect: community.network.ce_netconf
    ce_netstream_aging:
      redirect: community.network.ce_netstream_aging
    ce_netstream_export:
      redirect: community.network.ce_netstream_export
    ce_netstream_global:
      redirect: community.network.ce_netstream_global
    ce_netstream_template:
      redirect: community.network.ce_netstream_template
    ce_ntp:
      redirect: community.network.ce_ntp
    ce_ntp_auth:
      redirect: community.network.ce_ntp_auth
    ce_ospf:
      redirect: community.network.ce_ospf
    ce_ospf_vrf:
      redirect: community.network.ce_ospf_vrf
    ce_reboot:
      redirect: community.network.ce_reboot
    ce_rollback:
      redirect: community.network.ce_rollback
    ce_sflow:
      redirect: community.network.ce_sflow
    ce_snmp_community:
      redirect: community.network.ce_snmp_community
    ce_snmp_contact:
      redirect: community.network.ce_snmp_contact
    ce_snmp_location:
      redirect: community.network.ce_snmp_location
    ce_snmp_target_host:
      redirect: community.network.ce_snmp_target_host
    ce_snmp_traps:
      redirect: community.network.ce_snmp_traps
    ce_snmp_user:
      redirect: community.network.ce_snmp_user
    ce_startup:
      redirect: community.network.ce_startup
    ce_static_route:
      redirect: community.network.ce_static_route
    ce_static_route_bfd:
      redirect: community.network.ce_static_route_bfd
    ce_stp:
      redirect: community.network.ce_stp
    ce_switchport:
      redirect: community.network.ce_switchport
    ce_vlan:
      redirect: community.network.ce_vlan
    ce_vrf:
      redirect: community.network.ce_vrf
    ce_vrf_af:
      redirect: community.network.ce_vrf_af
    ce_vrf_interface:
      redirect: community.network.ce_vrf_interface
    ce_vrrp:
      redirect: community.network.ce_vrrp
    ce_vxlan_arp:
      redirect: community.network.ce_vxlan_arp
    ce_vxlan_gateway:
      redirect: community.network.ce_vxlan_gateway
    ce_vxlan_global:
      redirect: community.network.ce_vxlan_global
    ce_vxlan_tunnel:
      redirect: community.network.ce_vxlan_tunnel
    ce_vxlan_vap:
      redirect: community.network.ce_vxlan_vap
    cv_server_provision:
      redirect: community.network.cv_server_provision
    cnos_backup:
      redirect: community.network.cnos_backup
    cnos_banner:
      redirect: community.network.cnos_banner
    cnos_bgp:
      redirect: community.network.cnos_bgp
    cnos_command:
      redirect: community.network.cnos_command
    cnos_conditional_command:
      redirect: community.network.cnos_conditional_command
    cnos_conditional_template:
      redirect: community.network.cnos_conditional_template
    cnos_config:
      redirect: community.network.cnos_config
    cnos_factory:
      redirect: community.network.cnos_factory
    cnos_facts:
      redirect: community.network.cnos_facts
    cnos_image:
      redirect: community.network.cnos_image
    cnos_interface:
      redirect: community.network.cnos_interface
    cnos_l2_interface:
      redirect: community.network.cnos_l2_interface
    cnos_l3_interface:
      redirect: community.network.cnos_l3_interface
    cnos_linkagg:
      redirect: community.network.cnos_linkagg
    cnos_lldp:
      redirect: community.network.cnos_lldp
    cnos_logging:
      redirect: community.network.cnos_logging
    cnos_reload:
      redirect: community.network.cnos_reload
    cnos_rollback:
      redirect: community.network.cnos_rollback
    cnos_save:
      redirect: community.network.cnos_save
    cnos_showrun:
      redirect: community.network.cnos_showrun
    cnos_static_route:
      redirect: community.network.cnos_static_route
    cnos_system:
      redirect: community.network.cnos_system
    cnos_template:
      redirect: community.network.cnos_template
    cnos_user:
      redirect: community.network.cnos_user
    cnos_vlag:
      redirect: community.network.cnos_vlag
    cnos_vlan:
      redirect: community.network.cnos_vlan
    cnos_vrf:
      redirect: community.network.cnos_vrf
    nclu:
      redirect: community.network.nclu
    edgeos_command:
      redirect: community.network.edgeos_command
    edgeos_config:
      redirect: community.network.edgeos_config
    edgeos_facts:
      redirect: community.network.edgeos_facts
    edgeswitch_facts:
      redirect: community.network.edgeswitch_facts
    edgeswitch_vlan:
      redirect: community.network.edgeswitch_vlan
    enos_command:
      redirect: community.network.enos_command
    enos_config:
      redirect: community.network.enos_config
    enos_facts:
      redirect: community.network.enos_facts
    eric_eccli_command:
      redirect: community.network.eric_eccli_command
    exos_command:
      redirect: community.network.exos_command
    exos_config:
      redirect: community.network.exos_config
    exos_facts:
      redirect: community.network.exos_facts
    exos_l2_interfaces:
      redirect: community.network.exos_l2_interfaces
    exos_lldp_global:
      redirect: community.network.exos_lldp_global
    exos_lldp_interfaces:
      redirect: community.network.exos_lldp_interfaces
    exos_vlans:
      redirect: community.network.exos_vlans
    bigip_asm_policy:
      tombstone:
        removal_date: 2019-11-06
        warning_text: bigip_asm_policy has been removed please use bigip_asm_policy_manage instead.
    bigip_device_facts:
      redirect: f5networks.f5_modules.bigip_device_info
    bigip_iapplx_package:
      redirect: f5networks.f5_modules.bigip_lx_package
    bigip_security_address_list:
      redirect: f5networks.f5_modules.bigip_firewall_address_list
    bigip_security_port_list:
      redirect: f5networks.f5_modules.bigip_firewall_port_list
    bigip_traffic_group:
      redirect: f5networks.f5_modules.bigip_device_traffic_group
    bigip_facts:
      tombstone:
        removal_date: 2019-11-06
        warning_text: bigip_facts has been removed please use bigip_device_info module.
    bigip_gtm_facts:
      tombstone:
        removal_date: 2019-11-06
        warning_text: bigip_gtm_facts has been removed please use bigip_device_info module.
    faz_device:
      redirect: community.network.faz_device
    fmgr_device:
      redirect: community.network.fmgr_device
    fmgr_device_config:
      redirect: community.network.fmgr_device_config
    fmgr_device_group:
      redirect: community.network.fmgr_device_group
    fmgr_device_provision_template:
      redirect: community.network.fmgr_device_provision_template
    fmgr_fwobj_address:
      redirect: community.network.fmgr_fwobj_address
    fmgr_fwobj_ippool:
      redirect: community.network.fmgr_fwobj_ippool
    fmgr_fwobj_ippool6:
      redirect: community.network.fmgr_fwobj_ippool6
    fmgr_fwobj_service:
      redirect: community.network.fmgr_fwobj_service
    fmgr_fwobj_vip:
      redirect: community.network.fmgr_fwobj_vip
    fmgr_fwpol_ipv4:
      redirect: community.network.fmgr_fwpol_ipv4
    fmgr_fwpol_package:
      redirect: community.network.fmgr_fwpol_package
    fmgr_ha:
      redirect: community.network.fmgr_ha
    fmgr_provisioning:
      redirect: community.network.fmgr_provisioning
    fmgr_query:
      redirect: community.network.fmgr_query
    fmgr_script:
      redirect: community.network.fmgr_script
    fmgr_secprof_appctrl:
      redirect: community.network.fmgr_secprof_appctrl
    fmgr_secprof_av:
      redirect: community.network.fmgr_secprof_av
    fmgr_secprof_dns:
      redirect: community.network.fmgr_secprof_dns
    fmgr_secprof_ips:
      redirect: community.network.fmgr_secprof_ips
    fmgr_secprof_profile_group:
      redirect: community.network.fmgr_secprof_profile_group
    fmgr_secprof_proxy:
      redirect: community.network.fmgr_secprof_proxy
    fmgr_secprof_spam:
      redirect: community.network.fmgr_secprof_spam
    fmgr_secprof_ssl_ssh:
      redirect: community.network.fmgr_secprof_ssl_ssh
    fmgr_secprof_voip:
      redirect: community.network.fmgr_secprof_voip
    fmgr_secprof_waf:
      redirect: community.network.fmgr_secprof_waf
    fmgr_secprof_wanopt:
      redirect: community.network.fmgr_secprof_wanopt
    fmgr_secprof_web:
      redirect: community.network.fmgr_secprof_web
    ftd_configuration:
      redirect: community.network.ftd_configuration
    ftd_file_download:
      redirect: community.network.ftd_file_download
    ftd_file_upload:
      redirect: community.network.ftd_file_upload
    ftd_install:
      redirect: community.network.ftd_install
    icx_banner:
      redirect: community.network.icx_banner
    icx_command:
      redirect: community.network.icx_command
    icx_config:
      redirect: community.network.icx_config
    icx_copy:
      redirect: community.network.icx_copy
    icx_facts:
      redirect: community.network.icx_facts
    icx_interface:
      redirect: community.network.icx_interface
    icx_l3_interface:
      redirect: community.network.icx_l3_interface
    icx_linkagg:
      redirect: community.network.icx_linkagg
    icx_lldp:
      redirect: community.network.icx_lldp
    icx_logging:
      redirect: community.network.icx_logging
    icx_ping:
      redirect: community.network.icx_ping
    icx_static_route:
      redirect: community.network.icx_static_route
    icx_system:
      redirect: community.network.icx_system
    icx_user:
      redirect: community.network.icx_user
    icx_vlan:
      redirect: community.network.icx_vlan
    dladm_etherstub:
      redirect: community.network.dladm_etherstub
    dladm_iptun:
      redirect: community.network.dladm_iptun
    dladm_linkprop:
      redirect: community.network.dladm_linkprop
    dladm_vlan:
      redirect: community.network.dladm_vlan
    dladm_vnic:
      redirect: community.network.dladm_vnic
    flowadm:
      redirect: community.network.flowadm
    ipadm_addr:
      redirect: community.network.ipadm_addr
    ipadm_addrprop:
      redirect: community.network.ipadm_addrprop
    ipadm_if:
      redirect: community.network.ipadm_if
    ipadm_ifprop:
      redirect: community.network.ipadm_ifprop
    ipadm_prop:
      redirect: community.network.ipadm_prop
    ig_config:
      redirect: community.network.ig_config
    ig_unit_information:
      redirect: community.network.ig_unit_information
    ironware_command:
      redirect: community.network.ironware_command
    ironware_config:
      redirect: community.network.ironware_config
    ironware_facts:
      redirect: community.network.ironware_facts
    iap_start_workflow:
      redirect: community.network.iap_start_workflow
    iap_token:
      redirect: community.network.iap_token
    netact_cm_command:
      redirect: community.network.netact_cm_command
    netscaler_cs_action:
      redirect: community.network.netscaler_cs_action
    netscaler_cs_policy:
      redirect: community.network.netscaler_cs_policy
    netscaler_cs_vserver:
      redirect: community.network.netscaler_cs_vserver
    netscaler_gslb_service:
      redirect: community.network.netscaler_gslb_service
    netscaler_gslb_site:
      redirect: community.network.netscaler_gslb_site
    netscaler_gslb_vserver:
      redirect: community.network.netscaler_gslb_vserver
    netscaler_lb_monitor:
      redirect: community.network.netscaler_lb_monitor
    netscaler_lb_vserver:
      redirect: community.network.netscaler_lb_vserver
    netscaler_nitro_request:
      redirect: community.network.netscaler_nitro_request
    netscaler_save_config:
      redirect: community.network.netscaler_save_config
    netscaler_server:
      redirect: community.network.netscaler_server
    netscaler_service:
      redirect: community.network.netscaler_service
    netscaler_servicegroup:
      redirect: community.network.netscaler_servicegroup
    netscaler_ssl_certkey:
      redirect: community.network.netscaler_ssl_certkey
    pn_cluster:
      redirect: community.network.pn_cluster
    pn_ospf:
      redirect: community.network.pn_ospf
    pn_ospfarea:
      redirect: community.network.pn_ospfarea
    pn_show:
      redirect: community.network.pn_show
    pn_trunk:
      redirect: community.network.pn_trunk
    pn_vlag:
      redirect: community.network.pn_vlag
    pn_vlan:
      redirect: community.network.pn_vlan
    pn_vrouter:
      redirect: community.network.pn_vrouter
    pn_vrouterbgp:
      redirect: community.network.pn_vrouterbgp
    pn_vrouterif:
      redirect: community.network.pn_vrouterif
    pn_vrouterlbif:
      redirect: community.network.pn_vrouterlbif
    pn_access_list:
      redirect: community.network.pn_access_list
    pn_access_list_ip:
      redirect: community.network.pn_access_list_ip
    pn_admin_service:
      redirect: community.network.pn_admin_service
    pn_admin_session_timeout:
      redirect: community.network.pn_admin_session_timeout
    pn_admin_syslog:
      redirect: community.network.pn_admin_syslog
    pn_connection_stats_settings:
      redirect: community.network.pn_connection_stats_settings
    pn_cpu_class:
      redirect: community.network.pn_cpu_class
    pn_cpu_mgmt_class:
      redirect: community.network.pn_cpu_mgmt_class
    pn_dhcp_filter:
      redirect: community.network.pn_dhcp_filter
    pn_dscp_map:
      redirect: community.network.pn_dscp_map
    pn_dscp_map_pri_map:
      redirect: community.network.pn_dscp_map_pri_map
    pn_fabric_local:
      redirect: community.network.pn_fabric_local
    pn_igmp_snooping:
      redirect: community.network.pn_igmp_snooping
    pn_ipv6security_raguard:
      redirect: community.network.pn_ipv6security_raguard
    pn_ipv6security_raguard_port:
      redirect: community.network.pn_ipv6security_raguard_port
    pn_ipv6security_raguard_vlan:
      redirect: community.network.pn_ipv6security_raguard_vlan
    pn_log_audit_exception:
      redirect: community.network.pn_log_audit_exception
    pn_port_config:
      redirect: community.network.pn_port_config
    pn_port_cos_bw:
      redirect: community.network.pn_port_cos_bw
    pn_port_cos_rate_setting:
      redirect: community.network.pn_port_cos_rate_setting
    pn_prefix_list:
      redirect: community.network.pn_prefix_list
    pn_prefix_list_network:
      redirect: community.network.pn_prefix_list_network
    pn_role:
      redirect: community.network.pn_role
    pn_snmp_community:
      redirect: community.network.pn_snmp_community
    pn_snmp_trap_sink:
      redirect: community.network.pn_snmp_trap_sink
    pn_snmp_vacm:
      redirect: community.network.pn_snmp_vacm
    pn_stp:
      redirect: community.network.pn_stp
    pn_stp_port:
      redirect: community.network.pn_stp_port
    pn_switch_setup:
      redirect: community.network.pn_switch_setup
    pn_user:
      redirect: community.network.pn_user
    pn_vflow_table_profile:
      redirect: community.network.pn_vflow_table_profile
    pn_vrouter_bgp:
      redirect: community.network.pn_vrouter_bgp
    pn_vrouter_bgp_network:
      redirect: community.network.pn_vrouter_bgp_network
    pn_vrouter_interface_ip:
      redirect: community.network.pn_vrouter_interface_ip
    pn_vrouter_loopback_interface:
      redirect: community.network.pn_vrouter_loopback_interface
    pn_vrouter_ospf:
      redirect: community.network.pn_vrouter_ospf
    pn_vrouter_ospf6:
      redirect: community.network.pn_vrouter_ospf6
    pn_vrouter_packet_relay:
      redirect: community.network.pn_vrouter_packet_relay
    pn_vrouter_pim_config:
      redirect: community.network.pn_vrouter_pim_config
    pn_vtep:
      redirect: community.network.pn_vtep
    nos_command:
      redirect: community.network.nos_command
    nos_config:
      redirect: community.network.nos_config
    nos_facts:
      redirect: community.network.nos_facts
    nso_action:
      redirect: community.network.nso_action
    nso_config:
      redirect: community.network.nso_config
    nso_query:
      redirect: community.network.nso_query
    nso_show:
      redirect: community.network.nso_show
    nso_verify:
      redirect: community.network.nso_verify
    nuage_vspk:
      redirect: community.network.nuage_vspk
    onyx_aaa:
      redirect: mellanox.onyx.onyx_aaa
    onyx_bfd:
      redirect: mellanox.onyx.onyx_bfd
    onyx_bgp:
      redirect: mellanox.onyx.onyx_bgp
    onyx_buffer_pool:
      redirect: mellanox.onyx.onyx_buffer_pool
    onyx_command:
      redirect: mellanox.onyx.onyx_command
    onyx_config:
      redirect: mellanox.onyx.onyx_config
    onyx_facts:
      redirect: mellanox.onyx.onyx_facts
    onyx_igmp:
      redirect: mellanox.onyx.onyx_igmp
    onyx_igmp_interface:
      redirect: mellanox.onyx.onyx_igmp_interface
    onyx_igmp_vlan:
      redirect: mellanox.onyx.onyx_igmp_vlan
    onyx_interface:
      redirect: mellanox.onyx.onyx_interface
    onyx_l2_interface:
      redirect: mellanox.onyx.onyx_l2_interface
    onyx_l3_interface:
      redirect: mellanox.onyx.onyx_l3_interface
    onyx_linkagg:
      redirect: mellanox.onyx.onyx_linkagg
    onyx_lldp:
      redirect: mellanox.onyx.onyx_lldp
    onyx_lldp_interface:
      redirect: mellanox.onyx.onyx_lldp_interface
    onyx_magp:
      redirect: mellanox.onyx.onyx_magp
    onyx_mlag_ipl:
      redirect: mellanox.onyx.onyx_mlag_ipl
    onyx_mlag_vip:
      redirect: mellanox.onyx.onyx_mlag_vip
    onyx_ntp:
      redirect: mellanox.onyx.onyx_ntp
    onyx_ntp_servers_peers:
      redirect: mellanox.onyx.onyx_ntp_servers_peers
    onyx_ospf:
      redirect: mellanox.onyx.onyx_ospf
    onyx_pfc_interface:
      redirect: mellanox.onyx.onyx_pfc_interface
    onyx_protocol:
      redirect: mellanox.onyx.onyx_protocol
    onyx_ptp_global:
      redirect: mellanox.onyx.onyx_ptp_global
    onyx_ptp_interface:
      redirect: mellanox.onyx.onyx_ptp_interface
    onyx_qos:
      redirect: mellanox.onyx.onyx_qos
    onyx_snmp:
      redirect: mellanox.onyx.onyx_snmp
    onyx_snmp_hosts:
      redirect: mellanox.onyx.onyx_snmp_hosts
    onyx_snmp_users:
      redirect: mellanox.onyx.onyx_snmp_users
    onyx_syslog_files:
      redirect: mellanox.onyx.onyx_syslog_files
    onyx_syslog_remote:
      redirect: mellanox.onyx.onyx_syslog_remote
    onyx_traffic_class:
      redirect: mellanox.onyx.onyx_traffic_class
    onyx_username:
      redirect: mellanox.onyx.onyx_username
    onyx_vlan:
      redirect: mellanox.onyx.onyx_vlan
    onyx_vxlan:
      redirect: mellanox.onyx.onyx_vxlan
    onyx_wjh:
      redirect: mellanox.onyx.onyx_wjh
    opx_cps:
      redirect: community.network.opx_cps
    ordnance_config:
      redirect: community.network.ordnance_config
    ordnance_facts:
      redirect: community.network.ordnance_facts
    panos_admin:
      redirect: community.network.panos_admin
    panos_admpwd:
      redirect: community.network.panos_admpwd
    panos_cert_gen_ssh:
      redirect: community.network.panos_cert_gen_ssh
    panos_check:
      redirect: community.network.panos_check
    panos_commit:
      redirect: community.network.panos_commit
    panos_dag:
      redirect: community.network.panos_dag
    panos_dag_tags:
      redirect: community.network.panos_dag_tags
    panos_import:
      redirect: community.network.panos_import
    panos_interface:
      redirect: community.network.panos_interface
    panos_lic:
      redirect: community.network.panos_lic
    panos_loadcfg:
      redirect: community.network.panos_loadcfg
    panos_match_rule:
      redirect: community.network.panos_match_rule
    panos_mgtconfig:
      redirect: community.network.panos_mgtconfig
    panos_nat_rule:
      redirect: community.network.panos_nat_rule
    panos_object:
      redirect: community.network.panos_object
    panos_op:
      redirect: community.network.panos_op
    panos_pg:
      redirect: community.network.panos_pg
    panos_query_rules:
      redirect: community.network.panos_query_rules
    panos_restart:
      redirect: community.network.panos_restart
    panos_sag:
      redirect: community.network.panos_sag
    panos_security_rule:
      redirect: community.network.panos_security_rule
    panos_set:
      redirect: community.network.panos_set
    vdirect_commit:
      redirect: community.network.vdirect_commit
    vdirect_file:
      redirect: community.network.vdirect_file
    vdirect_runnable:
      redirect: community.network.vdirect_runnable
    routeros_command:
      redirect: community.network.routeros_command
    routeros_facts:
      redirect: community.network.routeros_facts
    slxos_command:
      redirect: community.network.slxos_command
    slxos_config:
      redirect: community.network.slxos_config
    slxos_facts:
      redirect: community.network.slxos_facts
    slxos_interface:
      redirect: community.network.slxos_interface
    slxos_l2_interface:
      redirect: community.network.slxos_l2_interface
    slxos_l3_interface:
      redirect: community.network.slxos_l3_interface
    slxos_linkagg:
      redirect: community.network.slxos_linkagg
    slxos_lldp:
      redirect: community.network.slxos_lldp
    slxos_vlan:
      redirect: community.network.slxos_vlan
    sros_command:
      redirect: community.network.sros_command
    sros_config:
      redirect: community.network.sros_config
    sros_rollback:
      redirect: community.network.sros_rollback
    voss_command:
      redirect: community.network.voss_command
    voss_config:
      redirect: community.network.voss_config
    voss_facts:
      redirect: community.network.voss_facts
    osx_say:
      redirect: community.general.say
    bearychat:
      redirect: community.general.bearychat
    campfire:
      redirect: community.general.campfire
    catapult:
      redirect: community.general.catapult
    cisco_spark:
      redirect: community.general.cisco_spark
    flowdock:
      redirect: community.general.flowdock
    grove:
      redirect: community.general.grove
    hipchat:
      redirect: community.general.hipchat
    irc:
      redirect: community.general.irc
    jabber:
      redirect: community.general.jabber
    logentries_msg:
      redirect: community.general.logentries_msg
    mail:
      redirect: community.general.mail
    matrix:
      redirect: community.general.matrix
    mattermost:
      redirect: community.general.mattermost
    mqtt:
      redirect: community.general.mqtt
    nexmo:
      redirect: community.general.nexmo
    office_365_connector_card:
      redirect: community.general.office_365_connector_card
    pushbullet:
      redirect: community.general.pushbullet
    pushover:
      redirect: community.general.pushover
    rabbitmq_publish:
      redirect: community.rabbitmq.rabbitmq_publish
    rocketchat:
      redirect: community.general.rocketchat
    say:
      redirect: community.general.say
    sendgrid:
      redirect: community.general.sendgrid
    slack:
      redirect: community.general.slack
    syslogger:
      redirect: community.general.syslogger
    telegram:
      redirect: community.general.telegram
    twilio:
      redirect: community.general.twilio
    typetalk:
      redirect: community.general.typetalk
    bower:
      redirect: community.general.bower
    bundler:
      redirect: community.general.bundler
    composer:
      redirect: community.general.composer
    cpanm:
      redirect: community.general.cpanm
    easy_install:
      redirect: community.general.easy_install
    gem:
      redirect: community.general.gem
    maven_artifact:
      redirect: community.general.maven_artifact
    npm:
      redirect: community.general.npm
    pear:
      redirect: community.general.pear
    pip_package_info:
      redirect: community.general.pip_package_info
    yarn:
      redirect: community.general.yarn
    apk:
      redirect: community.general.apk
    apt_rpm:
      redirect: community.general.apt_rpm
    flatpak:
      redirect: community.general.flatpak
    flatpak_remote:
      redirect: community.general.flatpak_remote
    homebrew:
      redirect: community.general.homebrew
    homebrew_cask:
      redirect: community.general.homebrew_cask
    homebrew_tap:
      redirect: community.general.homebrew_tap
    installp:
      redirect: community.general.installp
    layman:
      redirect: community.general.layman
    macports:
      redirect: community.general.macports
    mas:
      redirect: community.general.mas
    openbsd_pkg:
      redirect: community.general.openbsd_pkg
    opkg:
      redirect: community.general.opkg
    pacman:
      redirect: community.general.pacman
    pkg5:
      redirect: community.general.pkg5
    pkg5_publisher:
      redirect: community.general.pkg5_publisher
    pkgin:
      redirect: community.general.pkgin
    pkgng:
      redirect: community.general.pkgng
    pkgutil:
      redirect: community.general.pkgutil
    portage:
      redirect: community.general.portage
    portinstall:
      redirect: community.general.portinstall
    pulp_repo:
      redirect: community.general.pulp_repo
    redhat_subscription:
      redirect: community.general.redhat_subscription
    rhn_channel:
      redirect: community.general.rhn_channel
    rhn_register:
      redirect: community.general.rhn_register
    rhsm_release:
      redirect: community.general.rhsm_release
    rhsm_repository:
      redirect: community.general.rhsm_repository
    slackpkg:
      redirect: community.general.slackpkg
    snap:
      redirect: community.general.snap
    sorcery:
      redirect: community.general.sorcery
    svr4pkg:
      redirect: community.general.svr4pkg
    swdepot:
      redirect: community.general.swdepot
    swupd:
      redirect: community.general.swupd
    urpmi:
      redirect: community.general.urpmi
    xbps:
      redirect: community.general.xbps
    zypper:
      redirect: community.general.zypper
    zypper_repository:
      redirect: community.general.zypper_repository
    cobbler_sync:
      redirect: community.general.cobbler_sync
    cobbler_system:
      redirect: community.general.cobbler_system
    idrac_firmware:
      redirect: community.general.idrac_firmware
    idrac_server_config_profile:
      redirect: community.general.idrac_server_config_profile
    ome_device_info:
      redirect: community.general.ome_device_info
    foreman:
      redirect: community.general.foreman
    katello:
      redirect: community.general.katello
    hpilo_facts:
      redirect: community.general.hpilo_facts
    hpilo_boot:
      redirect: community.general.hpilo_boot
    hpilo_info:
      redirect: community.general.hpilo_info
    hponcfg:
      redirect: community.general.hponcfg
    imc_rest:
      redirect: community.general.imc_rest
    ipmi_boot:
      redirect: community.general.ipmi_boot
    ipmi_power:
      redirect: community.general.ipmi_power
    lxca_cmms:
      redirect: community.general.lxca_cmms
    lxca_nodes:
      redirect: community.general.lxca_nodes
    manageiq_alert_profiles:
      redirect: community.general.manageiq_alert_profiles
    manageiq_alerts:
      redirect: community.general.manageiq_alerts
    manageiq_group:
      redirect: community.general.manageiq_group
    manageiq_policies:
      redirect: community.general.manageiq_policies
    manageiq_provider:
      redirect: community.general.manageiq_provider
    manageiq_tags:
      redirect: community.general.manageiq_tags
    manageiq_tenant:
      redirect: community.general.manageiq_tenant
    manageiq_user:
      redirect: community.general.manageiq_user
    oneview_datacenter_facts:
      redirect: community.general.oneview_datacenter_facts
    oneview_enclosure_facts:
      redirect: community.general.oneview_enclosure_facts
    oneview_ethernet_network_facts:
      redirect: community.general.oneview_ethernet_network_facts
    oneview_fc_network_facts:
      redirect: community.general.oneview_fc_network_facts
    oneview_fcoe_network_facts:
      redirect: community.general.oneview_fcoe_network_facts
    oneview_logical_interconnect_group_facts:
      redirect: community.general.oneview_logical_interconnect_group_facts
    oneview_network_set_facts:
      redirect: community.general.oneview_network_set_facts
    oneview_san_manager_facts:
      redirect: community.general.oneview_san_manager_facts
    oneview_datacenter_info:
      redirect: community.general.oneview_datacenter_info
    oneview_enclosure_info:
      redirect: community.general.oneview_enclosure_info
    oneview_ethernet_network:
      redirect: community.general.oneview_ethernet_network
    oneview_ethernet_network_info:
      redirect: community.general.oneview_ethernet_network_info
    oneview_fc_network:
      redirect: community.general.oneview_fc_network
    oneview_fc_network_info:
      redirect: community.general.oneview_fc_network_info
    oneview_fcoe_network:
      redirect: community.general.oneview_fcoe_network
    oneview_fcoe_network_info:
      redirect: community.general.oneview_fcoe_network_info
    oneview_logical_interconnect_group:
      redirect: community.general.oneview_logical_interconnect_group
    oneview_logical_interconnect_group_info:
      redirect: community.general.oneview_logical_interconnect_group_info
    oneview_network_set:
      redirect: community.general.oneview_network_set
    oneview_network_set_info:
      redirect: community.general.oneview_network_set_info
    oneview_san_manager:
      redirect: community.general.oneview_san_manager
    oneview_san_manager_info:
      redirect: community.general.oneview_san_manager_info
    idrac_redfish_facts:
      redirect: community.general.idrac_redfish_facts
    redfish_facts:
      redirect: community.general.redfish_facts
    idrac_redfish_command:
      redirect: community.general.idrac_redfish_command
    idrac_redfish_config:
      redirect: community.general.idrac_redfish_config
    idrac_redfish_info:
      redirect: community.general.idrac_redfish_info
    redfish_command:
      redirect: community.general.redfish_command
    redfish_config:
      redirect: community.general.redfish_config
    redfish_info:
      redirect: community.general.redfish_info
    stacki_host:
      redirect: community.general.stacki_host
    wakeonlan:
      redirect: community.general.wakeonlan
    bitbucket_access_key:
      redirect: community.general.bitbucket_access_key
    bitbucket_pipeline_key_pair:
      redirect: community.general.bitbucket_pipeline_key_pair
    bitbucket_pipeline_known_host:
      redirect: community.general.bitbucket_pipeline_known_host
    bitbucket_pipeline_variable:
      redirect: community.general.bitbucket_pipeline_variable
    bzr:
      redirect: community.general.bzr
    git_config:
      redirect: community.general.git_config
    github_hooks:
      redirect: community.general.github_hooks
    github_webhook_facts:
      redirect: community.general.github_webhook_info
    github_deploy_key:
      redirect: community.general.github_deploy_key
    github_issue:
      redirect: community.general.github_issue
    github_key:
      redirect: community.general.github_key
    github_release:
      redirect: community.general.github_release
    github_webhook:
      redirect: community.general.github_webhook
    github_webhook_info:
      redirect: community.general.github_webhook_info
    gitlab_hooks:
      redirect: community.general.gitlab_hook
    gitlab_deploy_key:
      redirect: community.general.gitlab_deploy_key
    gitlab_group:
      redirect: community.general.gitlab_group
    gitlab_hook:
      redirect: community.general.gitlab_hook
    gitlab_project:
      redirect: community.general.gitlab_project
    gitlab_project_variable:
      redirect: community.general.gitlab_project_variable
    gitlab_runner:
      redirect: community.general.gitlab_runner
    gitlab_user:
      redirect: community.general.gitlab_user
    hg:
      redirect: community.general.hg
    emc_vnx_sg_member:
      redirect: community.general.emc_vnx_sg_member
    gluster_heal_facts:
      redirect: gluster.gluster.gluster_heal_info
    gluster_heal_info:
      redirect: gluster.gluster.gluster_heal_info
    gluster_peer:
      redirect: gluster.gluster.gluster_peer
    gluster_volume:
      redirect: gluster.gluster.gluster_volume
    ss_3par_cpg:
      redirect: community.general.ss_3par_cpg
    ibm_sa_domain:
      redirect: community.general.ibm_sa_domain
    ibm_sa_host:
      redirect: community.general.ibm_sa_host
    ibm_sa_host_ports:
      redirect: community.general.ibm_sa_host_ports
    ibm_sa_pool:
      redirect: community.general.ibm_sa_pool
    ibm_sa_vol:
      redirect: community.general.ibm_sa_vol
    ibm_sa_vol_map:
      redirect: community.general.ibm_sa_vol_map
    infini_export:
      redirect: infinidat.infinibox.infini_export
    infini_export_client:
      redirect: infinidat.infinibox.infini_export_client
    infini_fs:
      redirect: infinidat.infinibox.infini_fs
    infini_host:
      redirect: infinidat.infinibox.infini_host
    infini_pool:
      redirect: infinidat.infinibox.infini_pool
    infini_vol:
      redirect: infinidat.infinibox.infini_vol
    na_cdot_aggregate:
      redirect: community.general.na_cdot_aggregate
    na_cdot_license:
      redirect: community.general.na_cdot_license
    na_cdot_lun:
      redirect: community.general.na_cdot_lun
    na_cdot_qtree:
      redirect: community.general.na_cdot_qtree
    na_cdot_svm:
      redirect: community.general.na_cdot_svm
    na_cdot_user:
      redirect: community.general.na_cdot_user
    na_cdot_user_role:
      redirect: community.general.na_cdot_user_role
    na_cdot_volume:
      redirect: community.general.na_cdot_volume
    na_ontap_gather_facts:
      redirect: community.general.na_ontap_gather_facts
    sf_account_manager:
      redirect: community.general.sf_account_manager
    sf_check_connections:
      redirect: community.general.sf_check_connections
    sf_snapshot_schedule_manager:
      redirect: community.general.sf_snapshot_schedule_manager
    sf_volume_access_group_manager:
      redirect: community.general.sf_volume_access_group_manager
    sf_volume_manager:
      redirect: community.general.sf_volume_manager
    netapp_e_alerts:
      redirect: netapp_eseries.santricity.netapp_e_alerts
    netapp_e_amg:
      redirect: netapp_eseries.santricity.netapp_e_amg
    netapp_e_amg_role:
      redirect: netapp_eseries.santricity.netapp_e_amg_role
    netapp_e_amg_sync:
      redirect: netapp_eseries.santricity.netapp_e_amg_sync
    netapp_e_asup:
      redirect: netapp_eseries.santricity.netapp_e_asup
    netapp_e_auditlog:
      redirect: netapp_eseries.santricity.netapp_e_auditlog
    netapp_e_auth:
      redirect: netapp_eseries.santricity.netapp_e_auth
    netapp_e_drive_firmware:
      redirect: netapp_eseries.santricity.netapp_e_drive_firmware
    netapp_e_facts:
      redirect: netapp_eseries.santricity.netapp_e_facts
    netapp_e_firmware:
      redirect: netapp_eseries.santricity.netapp_e_firmware
    netapp_e_flashcache:
      redirect: netapp_eseries.santricity.netapp_e_flashcache
    netapp_e_global:
      redirect: netapp_eseries.santricity.netapp_e_global
    netapp_e_host:
      redirect: netapp_eseries.santricity.netapp_e_host
    netapp_e_hostgroup:
      redirect: netapp_eseries.santricity.netapp_e_hostgroup
    netapp_e_iscsi_interface:
      redirect: netapp_eseries.santricity.netapp_e_iscsi_interface
    netapp_e_iscsi_target:
      redirect: netapp_eseries.santricity.netapp_e_iscsi_target
    netapp_e_ldap:
      redirect: netapp_eseries.santricity.netapp_e_ldap
    netapp_e_lun_mapping:
      redirect: netapp_eseries.santricity.netapp_e_lun_mapping
    netapp_e_mgmt_interface:
      redirect: netapp_eseries.santricity.netapp_e_mgmt_interface
    netapp_e_snapshot_group:
      redirect: netapp_eseries.santricity.netapp_e_snapshot_group
    netapp_e_snapshot_images:
      redirect: netapp_eseries.santricity.netapp_e_snapshot_images
    netapp_e_snapshot_volume:
      redirect: netapp_eseries.santricity.netapp_e_snapshot_volume
    netapp_e_storage_system:
      redirect: netapp_eseries.santricity.netapp_e_storage_system
    netapp_e_storagepool:
      redirect: netapp_eseries.santricity.netapp_e_storagepool
    netapp_e_syslog:
      redirect: netapp_eseries.santricity.netapp_e_syslog
    netapp_e_volume:
      redirect: netapp_eseries.santricity.netapp_e_volume
    netapp_e_volume_copy:
      redirect: netapp_eseries.santricity.netapp_e_volume_copy
    purefa_facts:
      redirect: community.general.purefa_facts
    purefb_facts:
      redirect: community.general.purefb_facts
    vexata_eg:
      redirect: community.general.vexata_eg
    vexata_volume:
      redirect: community.general.vexata_volume
    zfs:
      redirect: community.general.zfs
    zfs_delegate_admin:
      redirect: community.general.zfs_delegate_admin
    zfs_facts:
      redirect: community.general.zfs_facts
    zpool_facts:
      redirect: community.general.zpool_facts
    python_requirements_facts:
      redirect: community.general.python_requirements_facts
    aix_devices:
      redirect: community.general.aix_devices
    aix_filesystem:
      redirect: community.general.aix_filesystem
    aix_inittab:
      redirect: community.general.aix_inittab
    aix_lvg:
      redirect: community.general.aix_lvg
    aix_lvol:
      redirect: community.general.aix_lvol
    alternatives:
      redirect: community.general.alternatives
    awall:
      redirect: community.general.awall
    beadm:
      redirect: community.general.beadm
    capabilities:
      redirect: community.general.capabilities
    cronvar:
      redirect: community.general.cronvar
    crypttab:
      redirect: community.general.crypttab
    dconf:
      redirect: community.general.dconf
    facter:
      redirect: community.general.facter
    filesystem:
      redirect: community.general.filesystem
    firewalld:
      redirect: ansible.posix.firewalld
    gconftool2:
      redirect: community.general.gconftool2
    interfaces_file:
      redirect: community.general.interfaces_file
    java_cert:
      redirect: community.general.java_cert
    java_keystore:
      redirect: community.general.java_keystore
    kernel_blacklist:
      redirect: community.general.kernel_blacklist
    lbu:
      redirect: community.general.lbu
    listen_ports_facts:
      redirect: community.general.listen_ports_facts
    locale_gen:
      redirect: community.general.locale_gen
    lvg:
      redirect: community.general.lvg
    lvol:
      redirect: community.general.lvol
    make:
      redirect: community.general.make
    mksysb:
      redirect: community.general.mksysb
    modprobe:
      redirect: community.general.modprobe
    nosh:
      redirect: community.general.nosh
    ohai:
      redirect: community.general.ohai
    open_iscsi:
      redirect: community.general.open_iscsi
    openwrt_init:
      redirect: community.general.openwrt_init
    osx_defaults:
      redirect: community.general.osx_defaults
    pam_limits:
      redirect: community.general.pam_limits
    pamd:
      redirect: community.general.pamd
    parted:
      redirect: community.general.parted
    pids:
      redirect: community.general.pids
    puppet:
      redirect: community.general.puppet
    python_requirements_info:
      redirect: community.general.python_requirements_info
    runit:
      redirect: community.general.runit
    sefcontext:
      redirect: community.general.sefcontext
    selinux_permissive:
      redirect: community.general.selinux_permissive
    selogin:
      redirect: community.general.selogin
    seport:
      redirect: community.general.seport
    solaris_zone:
      redirect: community.general.solaris_zone
    svc:
      redirect: community.general.svc
    syspatch:
      redirect: community.general.syspatch
    timezone:
      redirect: community.general.timezone
    ufw:
      redirect: community.general.ufw
    vdo:
      redirect: community.general.vdo
    xfconf:
      redirect: community.general.xfconf
    xfs_quota:
      redirect: community.general.xfs_quota
    jenkins_job_facts:
      redirect: community.general.jenkins_job_facts
    nginx_status_facts:
      redirect: community.general.nginx_status_facts
    apache2_mod_proxy:
      redirect: community.general.apache2_mod_proxy
    apache2_module:
      redirect: community.general.apache2_module
    deploy_helper:
      redirect: community.general.deploy_helper
    django_manage:
      redirect: community.general.django_manage
    ejabberd_user:
      redirect: community.general.ejabberd_user
    gunicorn:
      redirect: community.general.gunicorn
    htpasswd:
      redirect: community.general.htpasswd
    jboss:
      redirect: community.general.jboss
    jenkins_job:
      redirect: community.general.jenkins_job
    jenkins_job_info:
      redirect: community.general.jenkins_job_info
    jenkins_plugin:
      redirect: community.general.jenkins_plugin
    jenkins_script:
      redirect: community.general.jenkins_script
    jira:
      redirect: community.general.jira
    nginx_status_info:
      redirect: community.general.nginx_status_info
    rundeck_acl_policy:
      redirect: community.general.rundeck_acl_policy
    rundeck_project:
      redirect: community.general.rundeck_project
    utm_aaa_group:
      redirect: community.general.utm_aaa_group
    utm_aaa_group_info:
      redirect: community.general.utm_aaa_group_info
    utm_ca_host_key_cert:
      redirect: community.general.utm_ca_host_key_cert
    utm_ca_host_key_cert_info:
      redirect: community.general.utm_ca_host_key_cert_info
    utm_dns_host:
      redirect: community.general.utm_dns_host
    utm_network_interface_address:
      redirect: community.general.utm_network_interface_address
    utm_network_interface_address_info:
      redirect: community.general.utm_network_interface_address_info
    utm_proxy_auth_profile:
      redirect: community.general.utm_proxy_auth_profile
    utm_proxy_exception:
      redirect: community.general.utm_proxy_exception
    utm_proxy_frontend:
      redirect: community.general.utm_proxy_frontend
    utm_proxy_frontend_info:
      redirect: community.general.utm_proxy_frontend_info
    utm_proxy_location:
      redirect: community.general.utm_proxy_location
    utm_proxy_location_info:
      redirect: community.general.utm_proxy_location_info
    supervisorctl:
      redirect: community.general.supervisorctl
    taiga_issue:
      redirect: community.general.taiga_issue
    grafana_dashboard:
      redirect: community.grafana.grafana_dashboard
    grafana_datasource:
      redirect: community.grafana.grafana_datasource
    grafana_plugin:
      redirect: community.grafana.grafana_plugin
    k8s_facts:
      redirect: community.kubernetes.k8s_facts
    k8s_raw:
      redirect: community.kubernetes.k8s_raw
    k8s:
      redirect: community.kubernetes.k8s
    k8s_auth:
      redirect: community.kubernetes.k8s_auth
    k8s_info:
      redirect: community.kubernetes.k8s_info
    k8s_scale:
      redirect: community.kubernetes.k8s_scale
    k8s_service:
      redirect: community.kubernetes.k8s_service
    openshift_raw:
      redirect: community.kubernetes.openshift_raw
    openshift_scale:
      redirect: community.kubernetes.openshift_scale
    openssh_cert:
      redirect: community.crypto.openssh_cert
    openssl_pkcs12:
      redirect: community.crypto.openssl_pkcs12
    openssl_csr:
      redirect: community.crypto.openssl_csr
    openssl_certificate:
      redirect: community.crypto.x509_certificate
    openssl_certificate_info:
      redirect: community.crypto.x509_certificate_info
    x509_crl:
      redirect: community.crypto.x509_crl
    openssl_privatekey_info:
      redirect: community.crypto.openssl_privatekey_info
    x509_crl_info:
      redirect: community.crypto.x509_crl_info
    get_certificate:
      redirect: community.crypto.get_certificate
    openssh_keypair:
      redirect: community.crypto.openssh_keypair
    openssl_publickey:
      redirect: community.crypto.openssl_publickey
    openssl_csr_info:
      redirect: community.crypto.openssl_csr_info
    luks_device:
      redirect: community.crypto.luks_device
    openssl_dhparam:
      redirect: community.crypto.openssl_dhparam
    openssl_privatekey:
      redirect: community.crypto.openssl_privatekey
    certificate_complete_chain:
      redirect: community.crypto.certificate_complete_chain
    acme_inspect:
      redirect: community.crypto.acme_inspect
    acme_certificate_revoke:
      redirect: community.crypto.acme_certificate_revoke
    acme_certificate:
      redirect: community.crypto.acme_certificate
    acme_account:
      redirect: community.crypto.acme_account
    acme_account_facts:
      redirect: community.crypto.acme_account_facts
    acme_challenge_cert_helper:
      redirect: community.crypto.acme_challenge_cert_helper
    acme_account_info:
      redirect: community.crypto.acme_account_info
    ecs_domain:
      redirect: community.crypto.ecs_domain
    ecs_certificate:
      redirect: community.crypto.ecs_certificate
    mongodb_parameter:
      redirect: community.mongodb.mongodb_parameter
    mongodb_info:
      redirect: community.mongodb.mongodb_info
    mongodb_replicaset:
      redirect: community.mongodb.mongodb_replicaset
    mongodb_user:
      redirect: community.mongodb.mongodb_user
    mongodb_shard:
      redirect: community.mongodb.mongodb_shard
    vmware_appliance_access_info:
      redirect: vmware.vmware_rest.vmware_appliance_access_info
    vmware_appliance_health_info:
      redirect: vmware.vmware_rest.vmware_appliance_health_info
    vmware_cis_category_info:
      redirect: vmware.vmware_rest.vmware_cis_category_info
    vmware_core_info:
      redirect: vmware.vmware_rest.vmware_core_info
    vcenter_extension_facts:
      redirect: community.vmware.vcenter_extension_facts
    vmware_about_facts:
      redirect: community.vmware.vmware_about_facts
    vmware_category_facts:
      redirect: community.vmware.vmware_category_facts
    vmware_cluster_facts:
      redirect: community.vmware.vmware_cluster_facts
    vmware_datastore_facts:
      redirect: community.vmware.vmware_datastore_facts
    vmware_dns_config:
      redirect: community.vmware.vmware_dns_config
    vmware_drs_group_facts:
      redirect: community.vmware.vmware_drs_group_facts
    vmware_drs_rule_facts:
      redirect: community.vmware.vmware_drs_rule_facts
    vmware_dvs_portgroup_facts:
      redirect: community.vmware.vmware_dvs_portgroup_facts
    vmware_guest_boot_facts:
      redirect: community.vmware.vmware_guest_boot_facts
    vmware_guest_customization_facts:
      redirect: community.vmware.vmware_guest_customization_facts
    vmware_guest_disk_facts:
      redirect: community.vmware.vmware_guest_disk_facts
    vmware_guest_facts:
      redirect: community.vmware.vmware_guest_facts
    vmware_guest_snapshot_facts:
      redirect: community.vmware.vmware_guest_snapshot_facts
    vmware_host_capability_facts:
      redirect: community.vmware.vmware_host_capability_facts
    vmware_host_config_facts:
      redirect: community.vmware.vmware_host_config_facts
    vmware_host_dns_facts:
      redirect: community.vmware.vmware_host_dns_facts
    vmware_host_feature_facts:
      redirect: community.vmware.vmware_host_feature_facts
    vmware_host_firewall_facts:
      redirect: community.vmware.vmware_host_firewall_facts
    vmware_host_ntp_facts:
      redirect: community.vmware.vmware_host_ntp_facts
    vmware_host_package_facts:
      redirect: community.vmware.vmware_host_package_facts
    vmware_host_service_facts:
      redirect: community.vmware.vmware_host_service_facts
    vmware_host_ssl_facts:
      redirect: community.vmware.vmware_host_ssl_facts
    vmware_host_vmhba_facts:
      redirect: community.vmware.vmware_host_vmhba_facts
    vmware_host_vmnic_facts:
      redirect: community.vmware.vmware_host_vmnic_facts
    vmware_local_role_facts:
      redirect: community.vmware.vmware_local_role_facts
    vmware_local_user_facts:
      redirect: community.vmware.vmware_local_user_facts
    vmware_portgroup_facts:
      redirect: community.vmware.vmware_portgroup_facts
    vmware_resource_pool_facts:
      redirect: community.vmware.vmware_resource_pool_facts
    vmware_tag_facts:
      redirect: community.vmware.vmware_tag_facts
    vmware_target_canonical_facts:
      redirect: community.vmware.vmware_target_canonical_facts
    vmware_vm_facts:
      redirect: community.vmware.vmware_vm_facts
    vmware_vmkernel_facts:
      redirect: community.vmware.vmware_vmkernel_facts
    vmware_vswitch_facts:
      redirect: community.vmware.vmware_vswitch_facts
    vca_fw:
      redirect: community.vmware.vca_fw
    vca_nat:
      redirect: community.vmware.vca_nat
    vca_vapp:
      redirect: community.vmware.vca_vapp
    vcenter_extension:
      redirect: community.vmware.vcenter_extension
    vcenter_extension_info:
      redirect: community.vmware.vcenter_extension_info
    vcenter_folder:
      redirect: community.vmware.vcenter_folder
    vcenter_license:
      redirect: community.vmware.vcenter_license
    vmware_about_info:
      redirect: community.vmware.vmware_about_info
    vmware_category:
      redirect: community.vmware.vmware_category
    vmware_category_info:
      redirect: community.vmware.vmware_category_info
    vmware_cfg_backup:
      redirect: community.vmware.vmware_cfg_backup
    vmware_cluster:
      redirect: community.vmware.vmware_cluster
    vmware_cluster_drs:
      redirect: community.vmware.vmware_cluster_drs
    vmware_cluster_ha:
      redirect: community.vmware.vmware_cluster_ha
    vmware_cluster_info:
      redirect: community.vmware.vmware_cluster_info
    vmware_cluster_vsan:
      redirect: community.vmware.vmware_cluster_vsan
    vmware_content_deploy_template:
      redirect: community.vmware.vmware_content_deploy_template
    vmware_content_library_info:
      redirect: community.vmware.vmware_content_library_info
    vmware_content_library_manager:
      redirect: community.vmware.vmware_content_library_manager
    vmware_datacenter:
      redirect: community.vmware.vmware_datacenter
    vmware_datastore_cluster:
      redirect: community.vmware.vmware_datastore_cluster
    vmware_datastore_info:
      redirect: community.vmware.vmware_datastore_info
    vmware_datastore_maintenancemode:
      redirect: community.vmware.vmware_datastore_maintenancemode
    vmware_deploy_ovf:
      redirect: community.vmware.vmware_deploy_ovf
    vmware_drs_group:
      redirect: community.vmware.vmware_drs_group
    vmware_drs_group_info:
      redirect: community.vmware.vmware_drs_group_info
    vmware_drs_rule_info:
      redirect: community.vmware.vmware_drs_rule_info
    vmware_dvs_host:
      redirect: community.vmware.vmware_dvs_host
    vmware_dvs_portgroup:
      redirect: community.vmware.vmware_dvs_portgroup
    vmware_dvs_portgroup_find:
      redirect: community.vmware.vmware_dvs_portgroup_find
    vmware_dvs_portgroup_info:
      redirect: community.vmware.vmware_dvs_portgroup_info
    vmware_dvswitch:
      redirect: community.vmware.vmware_dvswitch
    vmware_dvswitch_lacp:
      redirect: community.vmware.vmware_dvswitch_lacp
    vmware_dvswitch_nioc:
      redirect: community.vmware.vmware_dvswitch_nioc
    vmware_dvswitch_pvlans:
      redirect: community.vmware.vmware_dvswitch_pvlans
    vmware_dvswitch_uplink_pg:
      redirect: community.vmware.vmware_dvswitch_uplink_pg
    vmware_evc_mode:
      redirect: community.vmware.vmware_evc_mode
    vmware_export_ovf:
      redirect: community.vmware.vmware_export_ovf
    vmware_folder_info:
      redirect: community.vmware.vmware_folder_info
    vmware_guest:
      redirect: community.vmware.vmware_guest
    vmware_guest_boot_info:
      redirect: community.vmware.vmware_guest_boot_info
    vmware_guest_boot_manager:
      redirect: community.vmware.vmware_guest_boot_manager
    vmware_guest_controller:
      redirect: community.vmware.vmware_guest_controller
    vmware_guest_cross_vc_clone:
      redirect: community.vmware.vmware_guest_cross_vc_clone
    vmware_guest_custom_attribute_defs:
      redirect: community.vmware.vmware_guest_custom_attribute_defs
    vmware_guest_custom_attributes:
      redirect: community.vmware.vmware_guest_custom_attributes
    vmware_guest_customization_info:
      redirect: community.vmware.vmware_guest_customization_info
    vmware_guest_disk:
      redirect: community.vmware.vmware_guest_disk
    vmware_guest_disk_info:
      redirect: community.vmware.vmware_guest_disk_info
    vmware_guest_file_operation:
      redirect: community.vmware.vmware_guest_file_operation
    vmware_guest_find:
      redirect: community.vmware.vmware_guest_find
    vmware_guest_info:
      redirect: community.vmware.vmware_guest_info
    vmware_guest_move:
      redirect: community.vmware.vmware_guest_move
    vmware_guest_network:
      redirect: community.vmware.vmware_guest_network
    vmware_guest_powerstate:
      redirect: community.vmware.vmware_guest_powerstate
    vmware_guest_register_operation:
      redirect: community.vmware.vmware_guest_register_operation
    vmware_guest_screenshot:
      redirect: community.vmware.vmware_guest_screenshot
    vmware_guest_sendkey:
      redirect: community.vmware.vmware_guest_sendkey
    vmware_guest_serial_port:
      redirect: community.vmware.vmware_guest_serial_port
    vmware_guest_snapshot:
      redirect: community.vmware.vmware_guest_snapshot
    vmware_guest_snapshot_info:
      redirect: community.vmware.vmware_guest_snapshot_info
    vmware_guest_tools_info:
      redirect: community.vmware.vmware_guest_tools_info
    vmware_guest_tools_upgrade:
      redirect: community.vmware.vmware_guest_tools_upgrade
    vmware_guest_tools_wait:
      redirect: community.vmware.vmware_guest_tools_wait
    vmware_guest_video:
      redirect: community.vmware.vmware_guest_video
    vmware_guest_vnc:
      redirect: community.vmware.vmware_guest_vnc
    vmware_host:
      redirect: community.vmware.vmware_host
    vmware_host_acceptance:
      redirect: community.vmware.vmware_host_acceptance
    vmware_host_active_directory:
      redirect: community.vmware.vmware_host_active_directory
    vmware_host_auto_start:
      redirect: community.vmware.vmware_host_auto_start
    vmware_host_capability_info:
      redirect: community.vmware.vmware_host_capability_info
    vmware_host_config_info:
      redirect: community.vmware.vmware_host_config_info
    vmware_host_config_manager:
      redirect: community.vmware.vmware_host_config_manager
    vmware_host_datastore:
      redirect: community.vmware.vmware_host_datastore
    vmware_host_dns:
      redirect: community.vmware.vmware_host_dns
    vmware_host_dns_info:
      redirect: community.vmware.vmware_host_dns_info
    vmware_host_facts:
      redirect: community.vmware.vmware_host_facts
    vmware_host_feature_info:
      redirect: community.vmware.vmware_host_feature_info
    vmware_host_firewall_info:
      redirect: community.vmware.vmware_host_firewall_info
    vmware_host_firewall_manager:
      redirect: community.vmware.vmware_host_firewall_manager
    vmware_host_hyperthreading:
      redirect: community.vmware.vmware_host_hyperthreading
    vmware_host_ipv6:
      redirect: community.vmware.vmware_host_ipv6
    vmware_host_kernel_manager:
      redirect: community.vmware.vmware_host_kernel_manager
    vmware_host_lockdown:
      redirect: community.vmware.vmware_host_lockdown
    vmware_host_ntp:
      redirect: community.vmware.vmware_host_ntp
    vmware_host_ntp_info:
      redirect: community.vmware.vmware_host_ntp_info
    vmware_host_package_info:
      redirect: community.vmware.vmware_host_package_info
    vmware_host_powermgmt_policy:
      redirect: community.vmware.vmware_host_powermgmt_policy
    vmware_host_powerstate:
      redirect: community.vmware.vmware_host_powerstate
    vmware_host_scanhba:
      redirect: community.vmware.vmware_host_scanhba
    vmware_host_service_info:
      redirect: community.vmware.vmware_host_service_info
    vmware_host_service_manager:
      redirect: community.vmware.vmware_host_service_manager
    vmware_host_snmp:
      redirect: community.vmware.vmware_host_snmp
    vmware_host_ssl_info:
      redirect: community.vmware.vmware_host_ssl_info
    vmware_host_vmhba_info:
      redirect: community.vmware.vmware_host_vmhba_info
    vmware_host_vmnic_info:
      redirect: community.vmware.vmware_host_vmnic_info
    vmware_local_role_info:
      redirect: community.vmware.vmware_local_role_info
    vmware_local_role_manager:
      redirect: community.vmware.vmware_local_role_manager
    vmware_local_user_info:
      redirect: community.vmware.vmware_local_user_info
    vmware_local_user_manager:
      redirect: community.vmware.vmware_local_user_manager
    vmware_maintenancemode:
      redirect: community.vmware.vmware_maintenancemode
    vmware_migrate_vmk:
      redirect: community.vmware.vmware_migrate_vmk
    vmware_object_role_permission:
      redirect: community.vmware.vmware_object_role_permission
    vmware_portgroup:
      redirect: community.vmware.vmware_portgroup
    vmware_portgroup_info:
      redirect: community.vmware.vmware_portgroup_info
    vmware_resource_pool:
      redirect: community.vmware.vmware_resource_pool
    vmware_resource_pool_info:
      redirect: community.vmware.vmware_resource_pool_info
    vmware_tag:
      redirect: community.vmware.vmware_tag
    vmware_tag_info:
      redirect: community.vmware.vmware_tag_info
    vmware_tag_manager:
      redirect: community.vmware.vmware_tag_manager
    vmware_target_canonical_info:
      redirect: community.vmware.vmware_target_canonical_info
    vmware_vcenter_settings:
      redirect: community.vmware.vmware_vcenter_settings
    vmware_vcenter_statistics:
      redirect: community.vmware.vmware_vcenter_statistics
    vmware_vm_host_drs_rule:
      redirect: community.vmware.vmware_vm_host_drs_rule
    vmware_vm_info:
      redirect: community.vmware.vmware_vm_info
    vmware_vm_shell:
      redirect: community.vmware.vmware_vm_shell
    vmware_vm_storage_policy_info:
      redirect: community.vmware.vmware_vm_storage_policy_info
    vmware_vm_vm_drs_rule:
      redirect: community.vmware.vmware_vm_vm_drs_rule
    vmware_vm_vss_dvs_migrate:
      redirect: community.vmware.vmware_vm_vss_dvs_migrate
    vmware_vmkernel:
      redirect: community.vmware.vmware_vmkernel
    vmware_vmkernel_info:
      redirect: community.vmware.vmware_vmkernel_info
    vmware_vmkernel_ip_config:
      redirect: community.vmware.vmware_vmkernel_ip_config
    vmware_vmotion:
      redirect: community.vmware.vmware_vmotion
    vmware_vsan_cluster:
      redirect: community.vmware.vmware_vsan_cluster
    vmware_vsan_health_info:
      redirect: community.vmware.vmware_vsan_health_info
    vmware_vspan_session:
      redirect: community.vmware.vmware_vspan_session
    vmware_vswitch:
      redirect: community.vmware.vmware_vswitch
    vmware_vswitch_info:
      redirect: community.vmware.vmware_vswitch_info
    vsphere_copy:
      redirect: community.vmware.vsphere_copy
    vsphere_file:
      redirect: community.vmware.vsphere_file
    psexec:
      redirect: community.windows.psexec
    win_audit_policy_system:
      redirect: community.windows.win_audit_policy_system
    win_audit_rule:
      redirect: community.windows.win_audit_rule
    win_chocolatey:
      redirect: chocolatey.chocolatey.win_chocolatey
    win_chocolatey_config:
      redirect: chocolatey.chocolatey.win_chocolatey_config
    win_chocolatey_facts:
      redirect: chocolatey.chocolatey.win_chocolatey_facts
    win_chocolatey_feature:
      redirect: chocolatey.chocolatey.win_chocolatey_feature
    win_chocolatey_source:
      redirect: chocolatey.chocolatey.win_chocolatey_source
    win_credential:
      redirect: community.windows.win_credential
    win_defrag:
      redirect: community.windows.win_defrag
    win_disk_facts:
      redirect: community.windows.win_disk_facts
    win_disk_image:
      redirect: community.windows.win_disk_image
    win_dns_record:
      redirect: community.windows.win_dns_record
    win_domain_computer:
      redirect: community.windows.win_domain_computer
    win_domain_group:
      redirect: community.windows.win_domain_group
    win_domain_group_membership:
      redirect: community.windows.win_domain_group_membership
    win_domain_user:
      redirect: community.windows.win_domain_user
    win_dotnet_ngen:
      redirect: community.windows.win_dotnet_ngen
    win_eventlog:
      redirect: community.windows.win_eventlog
    win_eventlog_entry:
      redirect: community.windows.win_eventlog_entry
    win_file_version:
      redirect: community.windows.win_file_version
    win_firewall:
      redirect: community.windows.win_firewall
    win_firewall_rule:
      redirect: community.windows.win_firewall_rule
    win_format:
      redirect: community.windows.win_format
    win_hosts:
      redirect: community.windows.win_hosts
    win_hotfix:
      redirect: community.windows.win_hotfix
    win_http_proxy:
      redirect: community.windows.win_http_proxy
    win_iis_virtualdirectory:
      redirect: community.windows.win_iis_virtualdirectory
    win_iis_webapplication:
      redirect: community.windows.win_iis_webapplication
    win_iis_webapppool:
      redirect: community.windows.win_iis_webapppool
    win_iis_webbinding:
      redirect: community.windows.win_iis_webbinding
    win_iis_website:
      redirect: community.windows.win_iis_website
    win_inet_proxy:
      redirect: community.windows.win_inet_proxy
    win_initialize_disk:
      redirect: community.windows.win_initialize_disk
    win_lineinfile:
      redirect: community.windows.win_lineinfile
    win_mapped_drive:
      redirect: community.windows.win_mapped_drive
    win_msg:
      redirect: community.windows.win_msg
    win_netbios:
      redirect: community.windows.win_netbios
    win_nssm:
      redirect: community.windows.win_nssm
    win_pagefile:
      redirect: community.windows.win_pagefile
    win_partition:
      redirect: community.windows.win_partition
    win_pester:
      redirect: community.windows.win_pester
    win_power_plan:
      redirect: community.windows.win_power_plan
    win_product_facts:
      redirect: community.windows.win_product_facts
    win_psexec:
      redirect: community.windows.win_psexec
    win_psmodule:
      redirect: community.windows.win_psmodule
    win_psrepository:
      redirect: community.windows.win_psrepository
    win_rabbitmq_plugin:
      redirect: community.windows.win_rabbitmq_plugin
    win_rds_cap:
      redirect: community.windows.win_rds_cap
    win_rds_rap:
      redirect: community.windows.win_rds_rap
    win_rds_settings:
      redirect: community.windows.win_rds_settings
    win_region:
      redirect: community.windows.win_region
    win_regmerge:
      redirect: community.windows.win_regmerge
    win_robocopy:
      redirect: community.windows.win_robocopy
    win_route:
      redirect: community.windows.win_route
    win_say:
      redirect: community.windows.win_say
    win_scheduled_task:
      redirect: community.windows.win_scheduled_task
    win_scheduled_task_stat:
      redirect: community.windows.win_scheduled_task_stat
    win_security_policy:
      redirect: community.windows.win_security_policy
    win_shortcut:
      redirect: community.windows.win_shortcut
    win_snmp:
      redirect: community.windows.win_snmp
    win_timezone:
      redirect: community.windows.win_timezone
    win_toast:
      redirect: community.windows.win_toast
    win_unzip:
      redirect: community.windows.win_unzip
    win_user_profile:
      redirect: community.windows.win_user_profile
    win_wait_for_process:
      redirect: community.windows.win_wait_for_process
    win_wakeonlan:
      redirect: community.windows.win_wakeonlan
    win_webpicmd:
      redirect: community.windows.win_webpicmd
    win_xml:
      redirect: community.windows.win_xml
    azure_rm_aks_facts:
      redirect: community.azure.azure_rm_aks_facts
    azure_rm_dnsrecordset_facts:
      redirect: community.azure.azure_rm_dnsrecordset_facts
    azure_rm_dnszone_facts:
      redirect: community.azure.azure_rm_dnszone_facts
    azure_rm_networkinterface_facts:
      redirect: community.azure.azure_rm_networkinterface_facts
    azure_rm_publicipaddress_facts:
      redirect: community.azure.azure_rm_publicipaddress_facts
    azure_rm_securitygroup_facts:
      redirect: community.azure.azure_rm_securitygroup_facts
    azure_rm_storageaccount_facts:
      redirect: community.azure.azure_rm_storageaccount_facts
    azure_rm_virtualmachine_facts:
      redirect: community.azure.azure_rm_virtualmachine_facts
    azure_rm_virtualnetwork_facts:
      redirect: community.azure.azure_rm_virtualnetwork_facts
    azure_rm_roledefinition_facts:
      redirect: community.azure.azure_rm_roledefinition_facts
    azure_rm_autoscale_facts:
      redirect: community.azure.azure_rm_autoscale_facts
    azure_rm_mysqldatabase_facts:
      redirect: community.azure.azure_rm_mysqldatabase_facts
    azure_rm_devtestlabschedule_facts:
      redirect: community.azure.azure_rm_devtestlabschedule_facts
    azure_rm_virtualmachinescaleset_facts:
      redirect: community.azure.azure_rm_virtualmachinescaleset_facts
    azure_rm_devtestlabcustomimage_facts:
      redirect: community.azure.azure_rm_devtestlabcustomimage_facts
    azure_rm_cosmosdbaccount_facts:
      redirect: community.azure.azure_rm_cosmosdbaccount_facts
    azure_rm_subnet_facts:
      redirect: community.azure.azure_rm_subnet_facts
    azure_rm_aksversion_facts:
      redirect: community.azure.azure_rm_aksversion_facts
    azure_rm_hdinsightcluster_facts:
      redirect: community.azure.azure_rm_hdinsightcluster_facts
    azure_rm_virtualmachinescalesetextension_facts:
      redirect: community.azure.azure_rm_virtualmachinescalesetextension_facts
    azure_rm_loadbalancer_facts:
      redirect: community.azure.azure_rm_loadbalancer_facts
    azure_rm_roleassignment_facts:
      redirect: community.azure.azure_rm_roleassignment_facts
    azure_rm_manageddisk_facts:
      redirect: community.azure.azure_rm_manageddisk_facts
    azure_rm_mysqlserver_facts:
      redirect: community.azure.azure_rm_mysqlserver_facts
    azure_rm_servicebus_facts:
      redirect: community.azure.azure_rm_servicebus_facts
    azure_rm_rediscache_facts:
      redirect: community.azure.azure_rm_rediscache_facts
    azure_rm_resource_facts:
      redirect: community.azure.azure_rm_resource_facts
    azure_rm_routetable_facts:
      redirect: community.azure.azure_rm_routetable_facts
    azure_rm_virtualmachine_extension:
      redirect: community.azure.azure_rm_virtualmachine_extension
    azure_rm_loganalyticsworkspace_facts:
      redirect: community.azure.azure_rm_loganalyticsworkspace_facts
    azure_rm_sqldatabase_facts:
      redirect: community.azure.azure_rm_sqldatabase_facts
    azure_rm_devtestlabartifactsource_facts:
      redirect: community.azure.azure_rm_devtestlabartifactsource_facts
    azure_rm_deployment_facts:
      redirect: community.azure.azure_rm_deployment_facts
    azure_rm_virtualmachineextension_facts:
      redirect: community.azure.azure_rm_virtualmachineextension_facts
    azure_rm_applicationsecuritygroup_facts:
      redirect: community.azure.azure_rm_applicationsecuritygroup_facts
    azure_rm_availabilityset_facts:
      redirect: community.azure.azure_rm_availabilityset_facts
    azure_rm_mariadbdatabase_facts:
      redirect: community.azure.azure_rm_mariadbdatabase_facts
    azure_rm_devtestlabenvironment_facts:
      redirect: community.azure.azure_rm_devtestlabenvironment_facts
    azure_rm_appserviceplan_facts:
      redirect: community.azure.azure_rm_appserviceplan_facts
    azure_rm_containerinstance_facts:
      redirect: community.azure.azure_rm_containerinstance_facts
    azure_rm_devtestlabarmtemplate_facts:
      redirect: community.azure.azure_rm_devtestlabarmtemplate_facts
    azure_rm_devtestlabartifact_facts:
      redirect: community.azure.azure_rm_devtestlabartifact_facts
    azure_rm_virtualmachinescalesetinstance_facts:
      redirect: community.azure.azure_rm_virtualmachinescalesetinstance_facts
    azure_rm_cdnendpoint_facts:
      redirect: community.azure.azure_rm_cdnendpoint_facts
    azure_rm_trafficmanagerprofile_facts:
      redirect: community.azure.azure_rm_trafficmanagerprofile_facts
    azure_rm_functionapp_facts:
      redirect: community.azure.azure_rm_functionapp_facts
    azure_rm_virtualmachineimage_facts:
      redirect: community.azure.azure_rm_virtualmachineimage_facts
    azure_rm_mariadbconfiguration_facts:
      redirect: community.azure.azure_rm_mariadbconfiguration_facts
    azure_rm_virtualnetworkpeering_facts:
      redirect: community.azure.azure_rm_virtualnetworkpeering_facts
    azure_rm_sqlserver_facts:
      redirect: community.azure.azure_rm_sqlserver_facts
    azure_rm_mariadbfirewallrule_facts:
      redirect: community.azure.azure_rm_mariadbfirewallrule_facts
    azure_rm_mysqlconfiguration_facts:
      redirect: community.azure.azure_rm_mysqlconfiguration_facts
    azure_rm_mysqlfirewallrule_facts:
      redirect: community.azure.azure_rm_mysqlfirewallrule_facts
    azure_rm_postgresqlfirewallrule_facts:
      redirect: community.azure.azure_rm_postgresqlfirewallrule_facts
    azure_rm_mariadbserver_facts:
      redirect: community.azure.azure_rm_mariadbserver_facts
    azure_rm_postgresqldatabase_facts:
      redirect: community.azure.azure_rm_postgresqldatabase_facts
    azure_rm_devtestlabvirtualnetwork_facts:
      redirect: community.azure.azure_rm_devtestlabvirtualnetwork_facts
    azure_rm_devtestlabpolicy_facts:
      redirect: community.azure.azure_rm_devtestlabpolicy_facts
    azure_rm_trafficmanagerendpoint_facts:
      redirect: community.azure.azure_rm_trafficmanagerendpoint_facts
    azure_rm_sqlfirewallrule_facts:
      redirect: community.azure.azure_rm_sqlfirewallrule_facts
    azure_rm_containerregistry_facts:
      redirect: community.azure.azure_rm_containerregistry_facts
    azure_rm_postgresqlconfiguration_facts:
      redirect: community.azure.azure_rm_postgresqlconfiguration_facts
    azure_rm_postgresqlserver_facts:
      redirect: community.azure.azure_rm_postgresqlserver_facts
    azure_rm_devtestlab_facts:
      redirect: community.azure.azure_rm_devtestlab_facts
    azure_rm_cdnprofile_facts:
      redirect: community.azure.azure_rm_cdnprofile_facts
    azure_rm_virtualmachine_scaleset:
      redirect: community.azure.azure_rm_virtualmachine_scaleset
    azure_rm_webapp_facts:
      redirect: community.azure.azure_rm_webapp_facts
    azure_rm_devtestlabvirtualmachine_facts:
      redirect: community.azure.azure_rm_devtestlabvirtualmachine_facts
    azure_rm_image_facts:
      redirect: community.azure.azure_rm_image_facts
    azure_rm_managed_disk:
      redirect: community.azure.azure_rm_managed_disk
    azure_rm_automationaccount_facts:
      redirect: community.azure.azure_rm_automationaccount_facts
    azure_rm_lock_facts:
      redirect: community.azure.azure_rm_lock_facts
    azure_rm_managed_disk_facts:
      redirect: community.azure.azure_rm_managed_disk_facts
    azure_rm_resourcegroup_facts:
      redirect: community.azure.azure_rm_resourcegroup_facts
    azure_rm_virtualmachine_scaleset_facts:
      redirect: community.azure.azure_rm_virtualmachine_scaleset_facts
    snow_record:
      redirect: servicenow.servicenow.snow_record
    snow_record_find:
      redirect: servicenow.servicenow.snow_record_find
    aws_az_facts:
      redirect: amazon.aws.aws_az_facts
    aws_caller_facts:
      redirect: amazon.aws.aws_caller_facts
    cloudformation_facts:
      redirect: amazon.aws.cloudformation_facts
    ec2_ami_facts:
      redirect: amazon.aws.ec2_ami_facts
    ec2_eni_facts:
      redirect: amazon.aws.ec2_eni_facts
    ec2_group_facts:
      redirect: amazon.aws.ec2_group_facts
    ec2_snapshot_facts:
      redirect: amazon.aws.ec2_snapshot_facts
    ec2_vol_facts:
      redirect: amazon.aws.ec2_vol_facts
    ec2_vpc_dhcp_option_facts:
      redirect: amazon.aws.ec2_vpc_dhcp_option_facts
    ec2_vpc_net_facts:
      redirect: amazon.aws.ec2_vpc_net_facts
    ec2_vpc_subnet_facts:
      redirect: amazon.aws.ec2_vpc_subnet_facts
    aws_az_info:
      redirect: amazon.aws.aws_az_info
    aws_caller_info:
      redirect: amazon.aws.aws_caller_info
    aws_s3:
      redirect: amazon.aws.aws_s3
    cloudformation:
      redirect: amazon.aws.cloudformation
    cloudformation_info:
      redirect: amazon.aws.cloudformation_info
    ec2:
      redirect: amazon.aws.ec2
    ec2_ami:
      redirect: amazon.aws.ec2_ami
    ec2_ami_info:
      redirect: amazon.aws.ec2_ami_info
    ec2_elb_lb:
      redirect: amazon.aws.ec2_elb_lb
    ec2_eni:
      redirect: amazon.aws.ec2_eni
    ec2_eni_info:
      redirect: amazon.aws.ec2_eni_info
    ec2_group:
      redirect: amazon.aws.ec2_group
    ec2_group_info:
      redirect: amazon.aws.ec2_group_info
    ec2_key:
      redirect: amazon.aws.ec2_key
    ec2_metadata_facts:
      redirect: amazon.aws.ec2_metadata_facts
    ec2_snapshot:
      redirect: amazon.aws.ec2_snapshot
    ec2_snapshot_info:
      redirect: amazon.aws.ec2_snapshot_info
    ec2_tag:
      redirect: amazon.aws.ec2_tag
    ec2_tag_info:
      redirect: amazon.aws.ec2_tag_info
    ec2_vol:
      redirect: amazon.aws.ec2_vol
    ec2_vol_info:
      redirect: amazon.aws.ec2_vol_info
    ec2_vpc_dhcp_option:
      redirect: amazon.aws.ec2_vpc_dhcp_option
    ec2_vpc_dhcp_option_info:
      redirect: amazon.aws.ec2_vpc_dhcp_option_info
    ec2_vpc_net:
      redirect: amazon.aws.ec2_vpc_net
    ec2_vpc_net_info:
      redirect: amazon.aws.ec2_vpc_net_info
    ec2_vpc_subnet:
      redirect: amazon.aws.ec2_vpc_subnet
    ec2_vpc_subnet_info:
      redirect: amazon.aws.ec2_vpc_subnet_info
    s3_bucket:
      redirect: amazon.aws.s3_bucket
    telnet:
      redirect: ansible.netcommon.telnet
    cli_command:
      redirect: ansible.netcommon.cli_command
    cli_config:
      redirect: ansible.netcommon.cli_config
    net_put:
      redirect: ansible.netcommon.net_put
    net_get:
      redirect: ansible.netcommon.net_get
    net_linkagg:
      redirect: ansible.netcommon.net_linkagg
    net_interface:
      redirect: ansible.netcommon.net_interface
    net_lldp_interface:
      redirect: ansible.netcommon.net_lldp_interface
    net_vlan:
      redirect: ansible.netcommon.net_vlan
    net_l2_interface:
      redirect: ansible.netcommon.net_l2_interface
    net_l3_interface:
      redirect: ansible.netcommon.net_l3_interface
    net_vrf:
      redirect: ansible.netcommon.net_vrf
    netconf_config:
      redirect: ansible.netcommon.netconf_config
    netconf_rpc:
      redirect: ansible.netcommon.netconf_rpc
    netconf_get:
      redirect: ansible.netcommon.netconf_get
    net_lldp:
      redirect: ansible.netcommon.net_lldp
    restconf_get:
      redirect: ansible.netcommon.restconf_get
    restconf_config:
      redirect: ansible.netcommon.restconf_config
    net_static_route:
      redirect: ansible.netcommon.net_static_route
    net_system:
      redirect: ansible.netcommon.net_system
    net_logging:
      redirect: ansible.netcommon.net_logging
    net_user:
      redirect: ansible.netcommon.net_user
    net_ping:
      redirect: ansible.netcommon.net_ping
    net_banner:
      redirect: ansible.netcommon.net_banner
    acl:
      redirect: ansible.posix.acl
    synchronize:
      redirect: ansible.posix.synchronize
    at:
      redirect: ansible.posix.at
    authorized_key:
      redirect: ansible.posix.authorized_key
    mount:
      redirect: ansible.posix.mount
    seboolean:
      redirect: ansible.posix.seboolean
    selinux:
      redirect: ansible.posix.selinux
    sysctl:
      redirect: ansible.posix.sysctl
    async_status.ps1:
      redirect: ansible.windows.async_status
    setup.ps1:
      redirect: ansible.windows.setup
    slurp.ps1:
      redirect: ansible.windows.slurp
    win_acl:
      redirect: ansible.windows.win_acl
    win_acl_inheritance:
      redirect: ansible.windows.win_acl_inheritance
    win_certificate_store:
      redirect: ansible.windows.win_certificate_store
    win_command:
      redirect: ansible.windows.win_command
    win_copy:
      redirect: ansible.windows.win_copy
    win_dns_client:
      redirect: ansible.windows.win_dns_client
    win_domain:
      redirect: ansible.windows.win_domain
    win_domain_controller:
      redirect: ansible.windows.win_domain_controller
    win_domain_membership:
      redirect: ansible.windows.win_domain_membership
    win_dsc:
      redirect: ansible.windows.win_dsc
    win_environment:
      redirect: ansible.windows.win_environment
    win_feature:
      redirect: ansible.windows.win_feature
    win_file:
      redirect: ansible.windows.win_file
    win_find:
      redirect: ansible.windows.win_find
    win_get_url:
      redirect: ansible.windows.win_get_url
    win_group:
      redirect: ansible.windows.win_group
    win_group_membership:
      redirect: ansible.windows.win_group_membership
    win_hostname:
      redirect: ansible.windows.win_hostname
    win_optional_feature:
      redirect: ansible.windows.win_optional_feature
    win_owner:
      redirect: ansible.windows.win_owner
    win_package:
      redirect: ansible.windows.win_package
    win_path:
      redirect: ansible.windows.win_path
    win_ping:
      redirect: ansible.windows.win_ping
    win_reboot:
      redirect: ansible.windows.win_reboot
    win_reg_stat:
      redirect: ansible.windows.win_reg_stat
    win_regedit:
      redirect: ansible.windows.win_regedit
    win_service:
      redirect: ansible.windows.win_service
    win_share:
      redirect: ansible.windows.win_share
    win_shell:
      redirect: ansible.windows.win_shell
    win_stat:
      redirect: ansible.windows.win_stat
    win_tempfile:
      redirect: ansible.windows.win_tempfile
    win_template:
      redirect: ansible.windows.win_template
    win_updates:
      redirect: ansible.windows.win_updates
    win_uri:
      redirect: ansible.windows.win_uri
    win_user:
      redirect: ansible.windows.win_user
    win_user_right:
      redirect: ansible.windows.win_user_right
    win_wait_for:
      redirect: ansible.windows.win_wait_for
    win_whoami:
      redirect: ansible.windows.win_whoami
    fortios_address:
      redirect: fortinet.fortios.fortios_address
    fortios_alertemail_setting:
      redirect: fortinet.fortios.fortios_alertemail_setting
    fortios_antivirus_heuristic:
      redirect: fortinet.fortios.fortios_antivirus_heuristic
    fortios_antivirus_profile:
      redirect: fortinet.fortios.fortios_antivirus_profile
    fortios_antivirus_quarantine:
      redirect: fortinet.fortios.fortios_antivirus_quarantine
    fortios_antivirus_settings:
      redirect: fortinet.fortios.fortios_antivirus_settings
    fortios_application_custom:
      redirect: fortinet.fortios.fortios_application_custom
    fortios_application_group:
      redirect: fortinet.fortios.fortios_application_group
    fortios_application_list:
      redirect: fortinet.fortios.fortios_application_list
    fortios_application_name:
      redirect: fortinet.fortios.fortios_application_name
    fortios_application_rule_settings:
      redirect: fortinet.fortios.fortios_application_rule_settings
    fortios_authentication_rule:
      redirect: fortinet.fortios.fortios_authentication_rule
    fortios_authentication_scheme:
      redirect: fortinet.fortios.fortios_authentication_scheme
    fortios_authentication_setting:
      redirect: fortinet.fortios.fortios_authentication_setting
    fortios_config:
      redirect: fortinet.fortios.fortios_config
    fortios_dlp_filepattern:
      redirect: fortinet.fortios.fortios_dlp_filepattern
    fortios_dlp_fp_doc_source:
      redirect: fortinet.fortios.fortios_dlp_fp_doc_source
    fortios_dlp_fp_sensitivity:
      redirect: fortinet.fortios.fortios_dlp_fp_sensitivity
    fortios_dlp_sensor:
      redirect: fortinet.fortios.fortios_dlp_sensor
    fortios_dlp_settings:
      redirect: fortinet.fortios.fortios_dlp_settings
    fortios_dnsfilter_domain_filter:
      redirect: fortinet.fortios.fortios_dnsfilter_domain_filter
    fortios_dnsfilter_profile:
      redirect: fortinet.fortios.fortios_dnsfilter_profile
    fortios_endpoint_control_client:
      redirect: fortinet.fortios.fortios_endpoint_control_client
    fortios_endpoint_control_forticlient_ems:
      redirect: fortinet.fortios.fortios_endpoint_control_forticlient_ems
    fortios_endpoint_control_forticlient_registration_sync:
      redirect: fortinet.fortios.fortios_endpoint_control_forticlient_registration_sync
    fortios_endpoint_control_profile:
      redirect: fortinet.fortios.fortios_endpoint_control_profile
    fortios_endpoint_control_settings:
      redirect: fortinet.fortios.fortios_endpoint_control_settings
    fortios_extender_controller_extender:
      redirect: fortinet.fortios.fortios_extender_controller_extender
    fortios_facts:
      redirect: fortinet.fortios.fortios_facts
    fortios_firewall_address:
      redirect: fortinet.fortios.fortios_firewall_address
    fortios_firewall_address6:
      redirect: fortinet.fortios.fortios_firewall_address6
    fortios_firewall_address6_template:
      redirect: fortinet.fortios.fortios_firewall_address6_template
    fortios_firewall_addrgrp:
      redirect: fortinet.fortios.fortios_firewall_addrgrp
    fortios_firewall_addrgrp6:
      redirect: fortinet.fortios.fortios_firewall_addrgrp6
    fortios_firewall_auth_portal:
      redirect: fortinet.fortios.fortios_firewall_auth_portal
    fortios_firewall_central_snat_map:
      redirect: fortinet.fortios.fortios_firewall_central_snat_map
    fortios_firewall_DoS_policy:
      redirect: fortinet.fortios.fortios_firewall_DoS_policy
    fortios_firewall_DoS_policy6:
      redirect: fortinet.fortios.fortios_firewall_DoS_policy6
    fortios_firewall_dnstranslation:
      redirect: fortinet.fortios.fortios_firewall_dnstranslation
    fortios_firewall_identity_based_route:
      redirect: fortinet.fortios.fortios_firewall_identity_based_route
    fortios_firewall_interface_policy:
      redirect: fortinet.fortios.fortios_firewall_interface_policy
    fortios_firewall_interface_policy6:
      redirect: fortinet.fortios.fortios_firewall_interface_policy6
    fortios_firewall_internet_service:
      redirect: fortinet.fortios.fortios_firewall_internet_service
    fortios_firewall_internet_service_custom:
      redirect: fortinet.fortios.fortios_firewall_internet_service_custom
    fortios_firewall_internet_service_group:
      redirect: fortinet.fortios.fortios_firewall_internet_service_group
    fortios_firewall_ip_translation:
      redirect: fortinet.fortios.fortios_firewall_ip_translation
    fortios_firewall_ipmacbinding_setting:
      redirect: fortinet.fortios.fortios_firewall_ipmacbinding_setting
    fortios_firewall_ipmacbinding_table:
      redirect: fortinet.fortios.fortios_firewall_ipmacbinding_table
    fortios_firewall_ippool:
      redirect: fortinet.fortios.fortios_firewall_ippool
    fortios_firewall_ippool6:
      redirect: fortinet.fortios.fortios_firewall_ippool6
    fortios_firewall_ipv6_eh_filter:
      redirect: fortinet.fortios.fortios_firewall_ipv6_eh_filter
    fortios_firewall_ldb_monitor:
      redirect: fortinet.fortios.fortios_firewall_ldb_monitor
    fortios_firewall_local_in_policy:
      redirect: fortinet.fortios.fortios_firewall_local_in_policy
    fortios_firewall_local_in_policy6:
      redirect: fortinet.fortios.fortios_firewall_local_in_policy6
    fortios_firewall_multicast_address:
      redirect: fortinet.fortios.fortios_firewall_multicast_address
    fortios_firewall_multicast_address6:
      redirect: fortinet.fortios.fortios_firewall_multicast_address6
    fortios_firewall_multicast_policy:
      redirect: fortinet.fortios.fortios_firewall_multicast_policy
    fortios_firewall_multicast_policy6:
      redirect: fortinet.fortios.fortios_firewall_multicast_policy6
    fortios_firewall_policy:
      redirect: fortinet.fortios.fortios_firewall_policy
    fortios_firewall_policy46:
      redirect: fortinet.fortios.fortios_firewall_policy46
    fortios_firewall_policy6:
      redirect: fortinet.fortios.fortios_firewall_policy6
    fortios_firewall_policy64:
      redirect: fortinet.fortios.fortios_firewall_policy64
    fortios_firewall_profile_group:
      redirect: fortinet.fortios.fortios_firewall_profile_group
    fortios_firewall_profile_protocol_options:
      redirect: fortinet.fortios.fortios_firewall_profile_protocol_options
    fortios_firewall_proxy_address:
      redirect: fortinet.fortios.fortios_firewall_proxy_address
    fortios_firewall_proxy_addrgrp:
      redirect: fortinet.fortios.fortios_firewall_proxy_addrgrp
    fortios_firewall_proxy_policy:
      redirect: fortinet.fortios.fortios_firewall_proxy_policy
    fortios_firewall_schedule_group:
      redirect: fortinet.fortios.fortios_firewall_schedule_group
    fortios_firewall_schedule_onetime:
      redirect: fortinet.fortios.fortios_firewall_schedule_onetime
    fortios_firewall_schedule_recurring:
      redirect: fortinet.fortios.fortios_firewall_schedule_recurring
    fortios_firewall_service_category:
      redirect: fortinet.fortios.fortios_firewall_service_category
    fortios_firewall_service_custom:
      redirect: fortinet.fortios.fortios_firewall_service_custom
    fortios_firewall_service_group:
      redirect: fortinet.fortios.fortios_firewall_service_group
    fortios_firewall_shaper_per_ip_shaper:
      redirect: fortinet.fortios.fortios_firewall_shaper_per_ip_shaper
    fortios_firewall_shaper_traffic_shaper:
      redirect: fortinet.fortios.fortios_firewall_shaper_traffic_shaper
    fortios_firewall_shaping_policy:
      redirect: fortinet.fortios.fortios_firewall_shaping_policy
    fortios_firewall_shaping_profile:
      redirect: fortinet.fortios.fortios_firewall_shaping_profile
    fortios_firewall_sniffer:
      redirect: fortinet.fortios.fortios_firewall_sniffer
    fortios_firewall_ssh_host_key:
      redirect: fortinet.fortios.fortios_firewall_ssh_host_key
    fortios_firewall_ssh_local_ca:
      redirect: fortinet.fortios.fortios_firewall_ssh_local_ca
    fortios_firewall_ssh_local_key:
      redirect: fortinet.fortios.fortios_firewall_ssh_local_key
    fortios_firewall_ssh_setting:
      redirect: fortinet.fortios.fortios_firewall_ssh_setting
    fortios_firewall_ssl_server:
      redirect: fortinet.fortios.fortios_firewall_ssl_server
    fortios_firewall_ssl_setting:
      redirect: fortinet.fortios.fortios_firewall_ssl_setting
    fortios_firewall_ssl_ssh_profile:
      redirect: fortinet.fortios.fortios_firewall_ssl_ssh_profile
    fortios_firewall_ttl_policy:
      redirect: fortinet.fortios.fortios_firewall_ttl_policy
    fortios_firewall_vip:
      redirect: fortinet.fortios.fortios_firewall_vip
    fortios_firewall_vip46:
      redirect: fortinet.fortios.fortios_firewall_vip46
    fortios_firewall_vip6:
      redirect: fortinet.fortios.fortios_firewall_vip6
    fortios_firewall_vip64:
      redirect: fortinet.fortios.fortios_firewall_vip64
    fortios_firewall_vipgrp:
      redirect: fortinet.fortios.fortios_firewall_vipgrp
    fortios_firewall_vipgrp46:
      redirect: fortinet.fortios.fortios_firewall_vipgrp46
    fortios_firewall_vipgrp6:
      redirect: fortinet.fortios.fortios_firewall_vipgrp6
    fortios_firewall_vipgrp64:
      redirect: fortinet.fortios.fortios_firewall_vipgrp64
    fortios_firewall_wildcard_fqdn_custom:
      redirect: fortinet.fortios.fortios_firewall_wildcard_fqdn_custom
    fortios_firewall_wildcard_fqdn_group:
      redirect: fortinet.fortios.fortios_firewall_wildcard_fqdn_group
    fortios_ftp_proxy_explicit:
      redirect: fortinet.fortios.fortios_ftp_proxy_explicit
    fortios_icap_profile:
      redirect: fortinet.fortios.fortios_icap_profile
    fortios_icap_server:
      redirect: fortinet.fortios.fortios_icap_server
    fortios_ips_custom:
      redirect: fortinet.fortios.fortios_ips_custom
    fortios_ips_decoder:
      redirect: fortinet.fortios.fortios_ips_decoder
    fortios_ips_global:
      redirect: fortinet.fortios.fortios_ips_global
    fortios_ips_rule:
      redirect: fortinet.fortios.fortios_ips_rule
    fortios_ips_rule_settings:
      redirect: fortinet.fortios.fortios_ips_rule_settings
    fortios_ips_sensor:
      redirect: fortinet.fortios.fortios_ips_sensor
    fortios_ips_settings:
      redirect: fortinet.fortios.fortios_ips_settings
    fortios_ipv4_policy:
      redirect: fortinet.fortios.fortios_ipv4_policy
    fortios_log_custom_field:
      redirect: fortinet.fortios.fortios_log_custom_field
    fortios_log_disk_filter:
      redirect: fortinet.fortios.fortios_log_disk_filter
    fortios_log_disk_setting:
      redirect: fortinet.fortios.fortios_log_disk_setting
    fortios_log_eventfilter:
      redirect: fortinet.fortios.fortios_log_eventfilter
    fortios_log_fortianalyzer2_filter:
      redirect: fortinet.fortios.fortios_log_fortianalyzer2_filter
    fortios_log_fortianalyzer2_setting:
      redirect: fortinet.fortios.fortios_log_fortianalyzer2_setting
    fortios_log_fortianalyzer3_filter:
      redirect: fortinet.fortios.fortios_log_fortianalyzer3_filter
    fortios_log_fortianalyzer3_setting:
      redirect: fortinet.fortios.fortios_log_fortianalyzer3_setting
    fortios_log_fortianalyzer_filter:
      redirect: fortinet.fortios.fortios_log_fortianalyzer_filter
    fortios_log_fortianalyzer_override_filter:
      redirect: fortinet.fortios.fortios_log_fortianalyzer_override_filter
    fortios_log_fortianalyzer_override_setting:
      redirect: fortinet.fortios.fortios_log_fortianalyzer_override_setting
    fortios_log_fortianalyzer_setting:
      redirect: fortinet.fortios.fortios_log_fortianalyzer_setting
    fortios_log_fortiguard_filter:
      redirect: fortinet.fortios.fortios_log_fortiguard_filter
    fortios_log_fortiguard_override_filter:
      redirect: fortinet.fortios.fortios_log_fortiguard_override_filter
    fortios_log_fortiguard_override_setting:
      redirect: fortinet.fortios.fortios_log_fortiguard_override_setting
    fortios_log_fortiguard_setting:
      redirect: fortinet.fortios.fortios_log_fortiguard_setting
    fortios_log_gui_display:
      redirect: fortinet.fortios.fortios_log_gui_display
    fortios_log_memory_filter:
      redirect: fortinet.fortios.fortios_log_memory_filter
    fortios_log_memory_global_setting:
      redirect: fortinet.fortios.fortios_log_memory_global_setting
    fortios_log_memory_setting:
      redirect: fortinet.fortios.fortios_log_memory_setting
    fortios_log_null_device_filter:
      redirect: fortinet.fortios.fortios_log_null_device_filter
    fortios_log_null_device_setting:
      redirect: fortinet.fortios.fortios_log_null_device_setting
    fortios_log_setting:
      redirect: fortinet.fortios.fortios_log_setting
    fortios_log_syslogd2_filter:
      redirect: fortinet.fortios.fortios_log_syslogd2_filter
    fortios_log_syslogd2_setting:
      redirect: fortinet.fortios.fortios_log_syslogd2_setting
    fortios_log_syslogd3_filter:
      redirect: fortinet.fortios.fortios_log_syslogd3_filter
    fortios_log_syslogd3_setting:
      redirect: fortinet.fortios.fortios_log_syslogd3_setting
    fortios_log_syslogd4_filter:
      redirect: fortinet.fortios.fortios_log_syslogd4_filter
    fortios_log_syslogd4_setting:
      redirect: fortinet.fortios.fortios_log_syslogd4_setting
    fortios_log_syslogd_filter:
      redirect: fortinet.fortios.fortios_log_syslogd_filter
    fortios_log_syslogd_override_filter:
      redirect: fortinet.fortios.fortios_log_syslogd_override_filter
    fortios_log_syslogd_override_setting:
      redirect: fortinet.fortios.fortios_log_syslogd_override_setting
    fortios_log_syslogd_setting:
      redirect: fortinet.fortios.fortios_log_syslogd_setting
    fortios_log_threat_weight:
      redirect: fortinet.fortios.fortios_log_threat_weight
    fortios_log_webtrends_filter:
      redirect: fortinet.fortios.fortios_log_webtrends_filter
    fortios_log_webtrends_setting:
      redirect: fortinet.fortios.fortios_log_webtrends_setting
    fortios_report_chart:
      redirect: fortinet.fortios.fortios_report_chart
    fortios_report_dataset:
      redirect: fortinet.fortios.fortios_report_dataset
    fortios_report_layout:
      redirect: fortinet.fortios.fortios_report_layout
    fortios_report_setting:
      redirect: fortinet.fortios.fortios_report_setting
    fortios_report_style:
      redirect: fortinet.fortios.fortios_report_style
    fortios_report_theme:
      redirect: fortinet.fortios.fortios_report_theme
    fortios_router_access_list:
      redirect: fortinet.fortios.fortios_router_access_list
    fortios_router_access_list6:
      redirect: fortinet.fortios.fortios_router_access_list6
    fortios_router_aspath_list:
      redirect: fortinet.fortios.fortios_router_aspath_list
    fortios_router_auth_path:
      redirect: fortinet.fortios.fortios_router_auth_path
    fortios_router_bfd:
      redirect: fortinet.fortios.fortios_router_bfd
    fortios_router_bfd6:
      redirect: fortinet.fortios.fortios_router_bfd6
    fortios_router_bgp:
      redirect: fortinet.fortios.fortios_router_bgp
    fortios_router_community_list:
      redirect: fortinet.fortios.fortios_router_community_list
    fortios_router_isis:
      redirect: fortinet.fortios.fortios_router_isis
    fortios_router_key_chain:
      redirect: fortinet.fortios.fortios_router_key_chain
    fortios_router_multicast:
      redirect: fortinet.fortios.fortios_router_multicast
    fortios_router_multicast6:
      redirect: fortinet.fortios.fortios_router_multicast6
    fortios_router_multicast_flow:
      redirect: fortinet.fortios.fortios_router_multicast_flow
    fortios_router_ospf:
      redirect: fortinet.fortios.fortios_router_ospf
    fortios_router_ospf6:
      redirect: fortinet.fortios.fortios_router_ospf6
    fortios_router_policy:
      redirect: fortinet.fortios.fortios_router_policy
    fortios_router_policy6:
      redirect: fortinet.fortios.fortios_router_policy6
    fortios_router_prefix_list:
      redirect: fortinet.fortios.fortios_router_prefix_list
    fortios_router_prefix_list6:
      redirect: fortinet.fortios.fortios_router_prefix_list6
    fortios_router_rip:
      redirect: fortinet.fortios.fortios_router_rip
    fortios_router_ripng:
      redirect: fortinet.fortios.fortios_router_ripng
    fortios_router_route_map:
      redirect: fortinet.fortios.fortios_router_route_map
    fortios_router_setting:
      redirect: fortinet.fortios.fortios_router_setting
    fortios_router_static:
      redirect: fortinet.fortios.fortios_router_static
    fortios_router_static6:
      redirect: fortinet.fortios.fortios_router_static6
    fortios_spamfilter_bwl:
      redirect: fortinet.fortios.fortios_spamfilter_bwl
    fortios_spamfilter_bword:
      redirect: fortinet.fortios.fortios_spamfilter_bword
    fortios_spamfilter_dnsbl:
      redirect: fortinet.fortios.fortios_spamfilter_dnsbl
    fortios_spamfilter_fortishield:
      redirect: fortinet.fortios.fortios_spamfilter_fortishield
    fortios_spamfilter_iptrust:
      redirect: fortinet.fortios.fortios_spamfilter_iptrust
    fortios_spamfilter_mheader:
      redirect: fortinet.fortios.fortios_spamfilter_mheader
    fortios_spamfilter_options:
      redirect: fortinet.fortios.fortios_spamfilter_options
    fortios_spamfilter_profile:
      redirect: fortinet.fortios.fortios_spamfilter_profile
    fortios_ssh_filter_profile:
      redirect: fortinet.fortios.fortios_ssh_filter_profile
    fortios_switch_controller_802_1X_settings:
      redirect: fortinet.fortios.fortios_switch_controller_802_1X_settings
    fortios_switch_controller_custom_command:
      redirect: fortinet.fortios.fortios_switch_controller_custom_command
    fortios_switch_controller_global:
      redirect: fortinet.fortios.fortios_switch_controller_global
    fortios_switch_controller_igmp_snooping:
      redirect: fortinet.fortios.fortios_switch_controller_igmp_snooping
    fortios_switch_controller_lldp_profile:
      redirect: fortinet.fortios.fortios_switch_controller_lldp_profile
    fortios_switch_controller_lldp_settings:
      redirect: fortinet.fortios.fortios_switch_controller_lldp_settings
    fortios_switch_controller_mac_sync_settings:
      redirect: fortinet.fortios.fortios_switch_controller_mac_sync_settings
    fortios_switch_controller_managed_switch:
      redirect: fortinet.fortios.fortios_switch_controller_managed_switch
    fortios_switch_controller_network_monitor_settings:
      redirect: fortinet.fortios.fortios_switch_controller_network_monitor_settings
    fortios_switch_controller_qos_dot1p_map:
      redirect: fortinet.fortios.fortios_switch_controller_qos_dot1p_map
    fortios_switch_controller_qos_ip_dscp_map:
      redirect: fortinet.fortios.fortios_switch_controller_qos_ip_dscp_map
    fortios_switch_controller_qos_qos_policy:
      redirect: fortinet.fortios.fortios_switch_controller_qos_qos_policy
    fortios_switch_controller_qos_queue_policy:
      redirect: fortinet.fortios.fortios_switch_controller_qos_queue_policy
    fortios_switch_controller_quarantine:
      redirect: fortinet.fortios.fortios_switch_controller_quarantine
    fortios_switch_controller_security_policy_802_1X:
      redirect: fortinet.fortios.fortios_switch_controller_security_policy_802_1X
    fortios_switch_controller_security_policy_captive_portal:
      redirect: fortinet.fortios.fortios_switch_controller_security_policy_captive_portal
    fortios_switch_controller_sflow:
      redirect: fortinet.fortios.fortios_switch_controller_sflow
    fortios_switch_controller_storm_control:
      redirect: fortinet.fortios.fortios_switch_controller_storm_control
    fortios_switch_controller_stp_settings:
      redirect: fortinet.fortios.fortios_switch_controller_stp_settings
    fortios_switch_controller_switch_group:
      redirect: fortinet.fortios.fortios_switch_controller_switch_group
    fortios_switch_controller_switch_interface_tag:
      redirect: fortinet.fortios.fortios_switch_controller_switch_interface_tag
    fortios_switch_controller_switch_log:
      redirect: fortinet.fortios.fortios_switch_controller_switch_log
    fortios_switch_controller_switch_profile:
      redirect: fortinet.fortios.fortios_switch_controller_switch_profile
    fortios_switch_controller_system:
      redirect: fortinet.fortios.fortios_switch_controller_system
    fortios_switch_controller_virtual_port_pool:
      redirect: fortinet.fortios.fortios_switch_controller_virtual_port_pool
    fortios_switch_controller_vlan:
      redirect: fortinet.fortios.fortios_switch_controller_vlan
    fortios_system_accprofile:
      redirect: fortinet.fortios.fortios_system_accprofile
    fortios_system_admin:
      redirect: fortinet.fortios.fortios_system_admin
    fortios_system_affinity_interrupt:
      redirect: fortinet.fortios.fortios_system_affinity_interrupt
    fortios_system_affinity_packet_redistribution:
      redirect: fortinet.fortios.fortios_system_affinity_packet_redistribution
    fortios_system_alarm:
      redirect: fortinet.fortios.fortios_system_alarm
    fortios_system_alias:
      redirect: fortinet.fortios.fortios_system_alias
    fortios_system_api_user:
      redirect: fortinet.fortios.fortios_system_api_user
    fortios_system_arp_table:
      redirect: fortinet.fortios.fortios_system_arp_table
    fortios_system_auto_install:
      redirect: fortinet.fortios.fortios_system_auto_install
    fortios_system_auto_script:
      redirect: fortinet.fortios.fortios_system_auto_script
    fortios_system_automation_action:
      redirect: fortinet.fortios.fortios_system_automation_action
    fortios_system_automation_destination:
      redirect: fortinet.fortios.fortios_system_automation_destination
    fortios_system_automation_stitch:
      redirect: fortinet.fortios.fortios_system_automation_stitch
    fortios_system_automation_trigger:
      redirect: fortinet.fortios.fortios_system_automation_trigger
    fortios_system_autoupdate_push_update:
      redirect: fortinet.fortios.fortios_system_autoupdate_push_update
    fortios_system_autoupdate_schedule:
      redirect: fortinet.fortios.fortios_system_autoupdate_schedule
    fortios_system_autoupdate_tunneling:
      redirect: fortinet.fortios.fortios_system_autoupdate_tunneling
    fortios_system_central_management:
      redirect: fortinet.fortios.fortios_system_central_management
    fortios_system_cluster_sync:
      redirect: fortinet.fortios.fortios_system_cluster_sync
    fortios_system_console:
      redirect: fortinet.fortios.fortios_system_console
    fortios_system_csf:
      redirect: fortinet.fortios.fortios_system_csf
    fortios_system_custom_language:
      redirect: fortinet.fortios.fortios_system_custom_language
    fortios_system_ddns:
      redirect: fortinet.fortios.fortios_system_ddns
    fortios_system_dedicated_mgmt:
      redirect: fortinet.fortios.fortios_system_dedicated_mgmt
    fortios_system_dhcp6_server:
      redirect: fortinet.fortios.fortios_system_dhcp6_server
    fortios_system_dhcp_server:
      redirect: fortinet.fortios.fortios_system_dhcp_server
    fortios_system_dns:
      redirect: fortinet.fortios.fortios_system_dns
    fortios_system_dns_database:
      redirect: fortinet.fortios.fortios_system_dns_database
    fortios_system_dns_server:
      redirect: fortinet.fortios.fortios_system_dns_server
    fortios_system_dscp_based_priority:
      redirect: fortinet.fortios.fortios_system_dscp_based_priority
    fortios_system_email_server:
      redirect: fortinet.fortios.fortios_system_email_server
    fortios_system_external_resource:
      redirect: fortinet.fortios.fortios_system_external_resource
    fortios_system_fips_cc:
      redirect: fortinet.fortios.fortios_system_fips_cc
    fortios_system_firmware_upgrade:
      redirect: fortinet.fortios.fortios_system_firmware_upgrade
    fortios_system_fm:
      redirect: fortinet.fortios.fortios_system_fm
    fortios_system_fortiguard:
      redirect: fortinet.fortios.fortios_system_fortiguard
    fortios_system_fortimanager:
      redirect: fortinet.fortios.fortios_system_fortimanager
    fortios_system_fortisandbox:
      redirect: fortinet.fortios.fortios_system_fortisandbox
    fortios_system_fsso_polling:
      redirect: fortinet.fortios.fortios_system_fsso_polling
    fortios_system_ftm_push:
      redirect: fortinet.fortios.fortios_system_ftm_push
    fortios_system_geoip_override:
      redirect: fortinet.fortios.fortios_system_geoip_override
    fortios_system_global:
      redirect: fortinet.fortios.fortios_system_global
    fortios_system_gre_tunnel:
      redirect: fortinet.fortios.fortios_system_gre_tunnel
    fortios_system_ha:
      redirect: fortinet.fortios.fortios_system_ha
    fortios_system_ha_monitor:
      redirect: fortinet.fortios.fortios_system_ha_monitor
    fortios_system_interface:
      redirect: fortinet.fortios.fortios_system_interface
    fortios_system_ipip_tunnel:
      redirect: fortinet.fortios.fortios_system_ipip_tunnel
    fortios_system_ips_urlfilter_dns:
      redirect: fortinet.fortios.fortios_system_ips_urlfilter_dns
    fortios_system_ips_urlfilter_dns6:
      redirect: fortinet.fortios.fortios_system_ips_urlfilter_dns6
    fortios_system_ipv6_neighbor_cache:
      redirect: fortinet.fortios.fortios_system_ipv6_neighbor_cache
    fortios_system_ipv6_tunnel:
      redirect: fortinet.fortios.fortios_system_ipv6_tunnel
    fortios_system_link_monitor:
      redirect: fortinet.fortios.fortios_system_link_monitor
    fortios_system_mac_address_table:
      redirect: fortinet.fortios.fortios_system_mac_address_table
    fortios_system_management_tunnel:
      redirect: fortinet.fortios.fortios_system_management_tunnel
    fortios_system_mobile_tunnel:
      redirect: fortinet.fortios.fortios_system_mobile_tunnel
    fortios_system_nat64:
      redirect: fortinet.fortios.fortios_system_nat64
    fortios_system_nd_proxy:
      redirect: fortinet.fortios.fortios_system_nd_proxy
    fortios_system_netflow:
      redirect: fortinet.fortios.fortios_system_netflow
    fortios_system_network_visibility:
      redirect: fortinet.fortios.fortios_system_network_visibility
    fortios_system_ntp:
      redirect: fortinet.fortios.fortios_system_ntp
    fortios_system_object_tagging:
      redirect: fortinet.fortios.fortios_system_object_tagging
    fortios_system_password_policy:
      redirect: fortinet.fortios.fortios_system_password_policy
    fortios_system_password_policy_guest_admin:
      redirect: fortinet.fortios.fortios_system_password_policy_guest_admin
    fortios_system_pppoe_interface:
      redirect: fortinet.fortios.fortios_system_pppoe_interface
    fortios_system_probe_response:
      redirect: fortinet.fortios.fortios_system_probe_response
    fortios_system_proxy_arp:
      redirect: fortinet.fortios.fortios_system_proxy_arp
    fortios_system_replacemsg_admin:
      redirect: fortinet.fortios.fortios_system_replacemsg_admin
    fortios_system_replacemsg_alertmail:
      redirect: fortinet.fortios.fortios_system_replacemsg_alertmail
    fortios_system_replacemsg_auth:
      redirect: fortinet.fortios.fortios_system_replacemsg_auth
    fortios_system_replacemsg_device_detection_portal:
      redirect: fortinet.fortios.fortios_system_replacemsg_device_detection_portal
    fortios_system_replacemsg_ec:
      redirect: fortinet.fortios.fortios_system_replacemsg_ec
    fortios_system_replacemsg_fortiguard_wf:
      redirect: fortinet.fortios.fortios_system_replacemsg_fortiguard_wf
    fortios_system_replacemsg_ftp:
      redirect: fortinet.fortios.fortios_system_replacemsg_ftp
    fortios_system_replacemsg_group:
      redirect: fortinet.fortios.fortios_system_replacemsg_group
    fortios_system_replacemsg_http:
      redirect: fortinet.fortios.fortios_system_replacemsg_http
    fortios_system_replacemsg_icap:
      redirect: fortinet.fortios.fortios_system_replacemsg_icap
    fortios_system_replacemsg_image:
      redirect: fortinet.fortios.fortios_system_replacemsg_image
    fortios_system_replacemsg_mail:
      redirect: fortinet.fortios.fortios_system_replacemsg_mail
    fortios_system_replacemsg_nac_quar:
      redirect: fortinet.fortios.fortios_system_replacemsg_nac_quar
    fortios_system_replacemsg_nntp:
      redirect: fortinet.fortios.fortios_system_replacemsg_nntp
    fortios_system_replacemsg_spam:
      redirect: fortinet.fortios.fortios_system_replacemsg_spam
    fortios_system_replacemsg_sslvpn:
      redirect: fortinet.fortios.fortios_system_replacemsg_sslvpn
    fortios_system_replacemsg_traffic_quota:
      redirect: fortinet.fortios.fortios_system_replacemsg_traffic_quota
    fortios_system_replacemsg_utm:
      redirect: fortinet.fortios.fortios_system_replacemsg_utm
    fortios_system_replacemsg_webproxy:
      redirect: fortinet.fortios.fortios_system_replacemsg_webproxy
    fortios_system_resource_limits:
      redirect: fortinet.fortios.fortios_system_resource_limits
    fortios_system_sdn_connector:
      redirect: fortinet.fortios.fortios_system_sdn_connector
    fortios_system_session_helper:
      redirect: fortinet.fortios.fortios_system_session_helper
    fortios_system_session_ttl:
      redirect: fortinet.fortios.fortios_system_session_ttl
    fortios_system_settings:
      redirect: fortinet.fortios.fortios_system_settings
    fortios_system_sflow:
      redirect: fortinet.fortios.fortios_system_sflow
    fortios_system_sit_tunnel:
      redirect: fortinet.fortios.fortios_system_sit_tunnel
    fortios_system_sms_server:
      redirect: fortinet.fortios.fortios_system_sms_server
    fortios_system_snmp_community:
      redirect: fortinet.fortios.fortios_system_snmp_community
    fortios_system_snmp_sysinfo:
      redirect: fortinet.fortios.fortios_system_snmp_sysinfo
    fortios_system_snmp_user:
      redirect: fortinet.fortios.fortios_system_snmp_user
    fortios_system_storage:
      redirect: fortinet.fortios.fortios_system_storage
    fortios_system_switch_interface:
      redirect: fortinet.fortios.fortios_system_switch_interface
    fortios_system_tos_based_priority:
      redirect: fortinet.fortios.fortios_system_tos_based_priority
    fortios_system_vdom:
      redirect: fortinet.fortios.fortios_system_vdom
    fortios_system_vdom_dns:
      redirect: fortinet.fortios.fortios_system_vdom_dns
    fortios_system_vdom_exception:
      redirect: fortinet.fortios.fortios_system_vdom_exception
    fortios_system_vdom_link:
      redirect: fortinet.fortios.fortios_system_vdom_link
    fortios_system_vdom_netflow:
      redirect: fortinet.fortios.fortios_system_vdom_netflow
    fortios_system_vdom_property:
      redirect: fortinet.fortios.fortios_system_vdom_property
    fortios_system_vdom_radius_server:
      redirect: fortinet.fortios.fortios_system_vdom_radius_server
    fortios_system_vdom_sflow:
      redirect: fortinet.fortios.fortios_system_vdom_sflow
    fortios_system_virtual_wan_link:
      redirect: fortinet.fortios.fortios_system_virtual_wan_link
    fortios_system_virtual_wire_pair:
      redirect: fortinet.fortios.fortios_system_virtual_wire_pair
    fortios_system_vxlan:
      redirect: fortinet.fortios.fortios_system_vxlan
    fortios_system_wccp:
      redirect: fortinet.fortios.fortios_system_wccp
    fortios_system_zone:
      redirect: fortinet.fortios.fortios_system_zone
    fortios_user_adgrp:
      redirect: fortinet.fortios.fortios_user_adgrp
    fortios_user_device:
      redirect: fortinet.fortios.fortios_user_device
    fortios_user_device_access_list:
      redirect: fortinet.fortios.fortios_user_device_access_list
    fortios_user_device_category:
      redirect: fortinet.fortios.fortios_user_device_category
    fortios_user_device_group:
      redirect: fortinet.fortios.fortios_user_device_group
    fortios_user_domain_controller:
      redirect: fortinet.fortios.fortios_user_domain_controller
    fortios_user_fortitoken:
      redirect: fortinet.fortios.fortios_user_fortitoken
    fortios_user_fsso:
      redirect: fortinet.fortios.fortios_user_fsso
    fortios_user_fsso_polling:
      redirect: fortinet.fortios.fortios_user_fsso_polling
    fortios_user_group:
      redirect: fortinet.fortios.fortios_user_group
    fortios_user_krb_keytab:
      redirect: fortinet.fortios.fortios_user_krb_keytab
    fortios_user_ldap:
      redirect: fortinet.fortios.fortios_user_ldap
    fortios_user_local:
      redirect: fortinet.fortios.fortios_user_local
    fortios_user_password_policy:
      redirect: fortinet.fortios.fortios_user_password_policy
    fortios_user_peer:
      redirect: fortinet.fortios.fortios_user_peer
    fortios_user_peergrp:
      redirect: fortinet.fortios.fortios_user_peergrp
    fortios_user_pop3:
      redirect: fortinet.fortios.fortios_user_pop3
    fortios_user_quarantine:
      redirect: fortinet.fortios.fortios_user_quarantine
    fortios_user_radius:
      redirect: fortinet.fortios.fortios_user_radius
    fortios_user_security_exempt_list:
      redirect: fortinet.fortios.fortios_user_security_exempt_list
    fortios_user_setting:
      redirect: fortinet.fortios.fortios_user_setting
    fortios_user_tacacsplus:
      redirect: fortinet.fortios.fortios_user_tacacsplus
    fortios_voip_profile:
      redirect: fortinet.fortios.fortios_voip_profile
    fortios_vpn_certificate_ca:
      redirect: fortinet.fortios.fortios_vpn_certificate_ca
    fortios_vpn_certificate_crl:
      redirect: fortinet.fortios.fortios_vpn_certificate_crl
    fortios_vpn_certificate_local:
      redirect: fortinet.fortios.fortios_vpn_certificate_local
    fortios_vpn_certificate_ocsp_server:
      redirect: fortinet.fortios.fortios_vpn_certificate_ocsp_server
    fortios_vpn_certificate_remote:
      redirect: fortinet.fortios.fortios_vpn_certificate_remote
    fortios_vpn_certificate_setting:
      redirect: fortinet.fortios.fortios_vpn_certificate_setting
    fortios_vpn_ipsec_concentrator:
      redirect: fortinet.fortios.fortios_vpn_ipsec_concentrator
    fortios_vpn_ipsec_forticlient:
      redirect: fortinet.fortios.fortios_vpn_ipsec_forticlient
    fortios_vpn_ipsec_manualkey:
      redirect: fortinet.fortios.fortios_vpn_ipsec_manualkey
    fortios_vpn_ipsec_manualkey_interface:
      redirect: fortinet.fortios.fortios_vpn_ipsec_manualkey_interface
    fortios_vpn_ipsec_phase1:
      redirect: fortinet.fortios.fortios_vpn_ipsec_phase1
    fortios_vpn_ipsec_phase1_interface:
      redirect: fortinet.fortios.fortios_vpn_ipsec_phase1_interface
    fortios_vpn_ipsec_phase2:
      redirect: fortinet.fortios.fortios_vpn_ipsec_phase2
    fortios_vpn_ipsec_phase2_interface:
      redirect: fortinet.fortios.fortios_vpn_ipsec_phase2_interface
    fortios_vpn_l2tp:
      redirect: fortinet.fortios.fortios_vpn_l2tp
    fortios_vpn_pptp:
      redirect: fortinet.fortios.fortios_vpn_pptp
    fortios_vpn_ssl_settings:
      redirect: fortinet.fortios.fortios_vpn_ssl_settings
    fortios_vpn_ssl_web_host_check_software:
      redirect: fortinet.fortios.fortios_vpn_ssl_web_host_check_software
    fortios_vpn_ssl_web_portal:
      redirect: fortinet.fortios.fortios_vpn_ssl_web_portal
    fortios_vpn_ssl_web_realm:
      redirect: fortinet.fortios.fortios_vpn_ssl_web_realm
    fortios_vpn_ssl_web_user_bookmark:
      redirect: fortinet.fortios.fortios_vpn_ssl_web_user_bookmark
    fortios_vpn_ssl_web_user_group_bookmark:
      redirect: fortinet.fortios.fortios_vpn_ssl_web_user_group_bookmark
    fortios_waf_main_class:
      redirect: fortinet.fortios.fortios_waf_main_class
    fortios_waf_profile:
      redirect: fortinet.fortios.fortios_waf_profile
    fortios_waf_signature:
      redirect: fortinet.fortios.fortios_waf_signature
    fortios_waf_sub_class:
      redirect: fortinet.fortios.fortios_waf_sub_class
    fortios_wanopt_auth_group:
      redirect: fortinet.fortios.fortios_wanopt_auth_group
    fortios_wanopt_cache_service:
      redirect: fortinet.fortios.fortios_wanopt_cache_service
    fortios_wanopt_content_delivery_network_rule:
      redirect: fortinet.fortios.fortios_wanopt_content_delivery_network_rule
    fortios_wanopt_peer:
      redirect: fortinet.fortios.fortios_wanopt_peer
    fortios_wanopt_profile:
      redirect: fortinet.fortios.fortios_wanopt_profile
    fortios_wanopt_remote_storage:
      redirect: fortinet.fortios.fortios_wanopt_remote_storage
    fortios_wanopt_settings:
      redirect: fortinet.fortios.fortios_wanopt_settings
    fortios_wanopt_webcache:
      redirect: fortinet.fortios.fortios_wanopt_webcache
    fortios_web_proxy_debug_url:
      redirect: fortinet.fortios.fortios_web_proxy_debug_url
    fortios_web_proxy_explicit:
      redirect: fortinet.fortios.fortios_web_proxy_explicit
    fortios_web_proxy_forward_server:
      redirect: fortinet.fortios.fortios_web_proxy_forward_server
    fortios_web_proxy_forward_server_group:
      redirect: fortinet.fortios.fortios_web_proxy_forward_server_group
    fortios_web_proxy_global:
      redirect: fortinet.fortios.fortios_web_proxy_global
    fortios_web_proxy_profile:
      redirect: fortinet.fortios.fortios_web_proxy_profile
    fortios_web_proxy_url_match:
      redirect: fortinet.fortios.fortios_web_proxy_url_match
    fortios_web_proxy_wisp:
      redirect: fortinet.fortios.fortios_web_proxy_wisp
    fortios_webfilter:
      redirect: fortinet.fortios.fortios_webfilter
    fortios_webfilter_content:
      redirect: fortinet.fortios.fortios_webfilter_content
    fortios_webfilter_content_header:
      redirect: fortinet.fortios.fortios_webfilter_content_header
    fortios_webfilter_fortiguard:
      redirect: fortinet.fortios.fortios_webfilter_fortiguard
    fortios_webfilter_ftgd_local_cat:
      redirect: fortinet.fortios.fortios_webfilter_ftgd_local_cat
    fortios_webfilter_ftgd_local_rating:
      redirect: fortinet.fortios.fortios_webfilter_ftgd_local_rating
    fortios_webfilter_ips_urlfilter_cache_setting:
      redirect: fortinet.fortios.fortios_webfilter_ips_urlfilter_cache_setting
    fortios_webfilter_ips_urlfilter_setting:
      redirect: fortinet.fortios.fortios_webfilter_ips_urlfilter_setting
    fortios_webfilter_ips_urlfilter_setting6:
      redirect: fortinet.fortios.fortios_webfilter_ips_urlfilter_setting6
    fortios_webfilter_override:
      redirect: fortinet.fortios.fortios_webfilter_override
    fortios_webfilter_profile:
      redirect: fortinet.fortios.fortios_webfilter_profile
    fortios_webfilter_search_engine:
      redirect: fortinet.fortios.fortios_webfilter_search_engine
    fortios_webfilter_urlfilter:
      redirect: fortinet.fortios.fortios_webfilter_urlfilter
    fortios_wireless_controller_ap_status:
      redirect: fortinet.fortios.fortios_wireless_controller_ap_status
    fortios_wireless_controller_ble_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_ble_profile
    fortios_wireless_controller_bonjour_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_bonjour_profile
    fortios_wireless_controller_global:
      redirect: fortinet.fortios.fortios_wireless_controller_global
    fortios_wireless_controller_hotspot20_anqp_3gpp_cellular:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_3gpp_cellular
    fortios_wireless_controller_hotspot20_anqp_ip_address_type:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_ip_address_type
    fortios_wireless_controller_hotspot20_anqp_nai_realm:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_nai_realm
    fortios_wireless_controller_hotspot20_anqp_network_auth_type:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_network_auth_type
    fortios_wireless_controller_hotspot20_anqp_roaming_consortium:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_roaming_consortium
    fortios_wireless_controller_hotspot20_anqp_venue_name:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_anqp_venue_name
    fortios_wireless_controller_hotspot20_h2qp_conn_capability:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_h2qp_conn_capability
    fortios_wireless_controller_hotspot20_h2qp_operator_name:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_h2qp_operator_name
    fortios_wireless_controller_hotspot20_h2qp_osu_provider:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_h2qp_osu_provider
    fortios_wireless_controller_hotspot20_h2qp_wan_metric:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_h2qp_wan_metric
    fortios_wireless_controller_hotspot20_hs_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_hs_profile
    fortios_wireless_controller_hotspot20_icon:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_icon
    fortios_wireless_controller_hotspot20_qos_map:
      redirect: fortinet.fortios.fortios_wireless_controller_hotspot20_qos_map
    fortios_wireless_controller_inter_controller:
      redirect: fortinet.fortios.fortios_wireless_controller_inter_controller
    fortios_wireless_controller_qos_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_qos_profile
    fortios_wireless_controller_setting:
      redirect: fortinet.fortios.fortios_wireless_controller_setting
    fortios_wireless_controller_timers:
      redirect: fortinet.fortios.fortios_wireless_controller_timers
    fortios_wireless_controller_utm_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_utm_profile
    fortios_wireless_controller_vap:
      redirect: fortinet.fortios.fortios_wireless_controller_vap
    fortios_wireless_controller_vap_group:
      redirect: fortinet.fortios.fortios_wireless_controller_vap_group
    fortios_wireless_controller_wids_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_wids_profile
    fortios_wireless_controller_wtp:
      redirect: fortinet.fortios.fortios_wireless_controller_wtp
    fortios_wireless_controller_wtp_group:
      redirect: fortinet.fortios.fortios_wireless_controller_wtp_group
    fortios_wireless_controller_wtp_profile:
      redirect: fortinet.fortios.fortios_wireless_controller_wtp_profile
    netbox_device:
      redirect: netbox.netbox.netbox_device
    netbox_ip_address:
      redirect: netbox.netbox.netbox_ip_address
    netbox_interface:
      redirect: netbox.netbox.netbox_interface
    netbox_prefix:
      redirect: netbox.netbox.netbox_prefix
    netbox_site:
      redirect: netbox.netbox.netbox_site
    aws_netapp_cvs_FileSystems:
      redirect: netapp.aws.aws_netapp_cvs_filesystems
    aws_netapp_cvs_active_directory:
      redirect: netapp.aws.aws_netapp_cvs_active_directory
    aws_netapp_cvs_pool:
      redirect: netapp.aws.aws_netapp_cvs_pool
    aws_netapp_cvs_snapshots:
      redirect: netapp.aws.aws_netapp_cvs_snapshots
    na_elementsw_access_group:
      redirect: netapp.elementsw.na_elementsw_access_group
    na_elementsw_account:
      redirect: netapp.elementsw.na_elementsw_account
    na_elementsw_admin_users:
      redirect: netapp.elementsw.na_elementsw_admin_users
    na_elementsw_backup:
      redirect: netapp.elementsw.na_elementsw_backup
    na_elementsw_check_connections:
      redirect: netapp.elementsw.na_elementsw_check_connections
    na_elementsw_cluster:
      redirect: netapp.elementsw.na_elementsw_cluster
    na_elementsw_cluster_config:
      redirect: netapp.elementsw.na_elementsw_cluster_config
    na_elementsw_cluster_pair:
      redirect: netapp.elementsw.na_elementsw_cluster_pair
    na_elementsw_cluster_snmp:
      redirect: netapp.elementsw.na_elementsw_cluster_snmp
    na_elementsw_drive:
      redirect: netapp.elementsw.na_elementsw_drive
    na_elementsw_initiators:
      redirect: netapp.elementsw.na_elementsw_initiators
    na_elementsw_ldap:
      redirect: netapp.elementsw.na_elementsw_ldap
    na_elementsw_network_interfaces:
      redirect: netapp.elementsw.na_elementsw_network_interfaces
    na_elementsw_node:
      redirect: netapp.elementsw.na_elementsw_node
    na_elementsw_snapshot:
      redirect: netapp.elementsw.na_elementsw_snapshot
    na_elementsw_snapshot_restore:
      redirect: netapp.elementsw.na_elementsw_snapshot_restore
    na_elementsw_snapshot_schedule:
      redirect: netapp.elementsw.na_elementsw_snapshot_schedule
    na_elementsw_vlan:
      redirect: netapp.elementsw.na_elementsw_vlan
    na_elementsw_volume:
      redirect: netapp.elementsw.na_elementsw_volume
    na_elementsw_volume_clone:
      redirect: netapp.elementsw.na_elementsw_volume_clone
    na_elementsw_volume_pair:
      redirect: netapp.elementsw.na_elementsw_volume_pair
    na_ontap_aggregate:
      redirect: netapp.ontap.na_ontap_aggregate
    na_ontap_autosupport:
      redirect: netapp.ontap.na_ontap_autosupport
    na_ontap_broadcast_domain:
      redirect: netapp.ontap.na_ontap_broadcast_domain
    na_ontap_broadcast_domain_ports:
      redirect: netapp.ontap.na_ontap_broadcast_domain_ports
    na_ontap_cg_snapshot:
      redirect: netapp.ontap.na_ontap_cg_snapshot
    na_ontap_cifs:
      redirect: netapp.ontap.na_ontap_cifs
    na_ontap_cifs_acl:
      redirect: netapp.ontap.na_ontap_cifs_acl
    na_ontap_cifs_server:
      redirect: netapp.ontap.na_ontap_cifs_server
    na_ontap_cluster:
      redirect: netapp.ontap.na_ontap_cluster
    na_ontap_cluster_ha:
      redirect: netapp.ontap.na_ontap_cluster_ha
    na_ontap_cluster_peer:
      redirect: netapp.ontap.na_ontap_cluster_peer
    na_ontap_command:
      redirect: netapp.ontap.na_ontap_command
    na_ontap_disks:
      redirect: netapp.ontap.na_ontap_disks
    na_ontap_dns:
      redirect: netapp.ontap.na_ontap_dns
    na_ontap_export_policy:
      redirect: netapp.ontap.na_ontap_export_policy
    na_ontap_export_policy_rule:
      redirect: netapp.ontap.na_ontap_export_policy_rule
    na_ontap_fcp:
      redirect: netapp.ontap.na_ontap_fcp
    na_ontap_firewall_policy:
      redirect: netapp.ontap.na_ontap_firewall_policy
    na_ontap_firmware_upgrade:
      redirect: netapp.ontap.na_ontap_firmware_upgrade
    na_ontap_flexcache:
      redirect: netapp.ontap.na_ontap_flexcache
    na_ontap_igroup:
      redirect: netapp.ontap.na_ontap_igroup
    na_ontap_igroup_initiator:
      redirect: netapp.ontap.na_ontap_igroup_initiator
    na_ontap_info:
      redirect: netapp.ontap.na_ontap_info
    na_ontap_interface:
      redirect: netapp.ontap.na_ontap_interface
    na_ontap_ipspace:
      redirect: netapp.ontap.na_ontap_ipspace
    na_ontap_iscsi:
      redirect: netapp.ontap.na_ontap_iscsi
    na_ontap_job_schedule:
      redirect: netapp.ontap.na_ontap_job_schedule
    na_ontap_kerberos_realm:
      redirect: netapp.ontap.na_ontap_kerberos_realm
    na_ontap_ldap:
      redirect: netapp.ontap.na_ontap_ldap
    na_ontap_ldap_client:
      redirect: netapp.ontap.na_ontap_ldap_client
    na_ontap_license:
      redirect: netapp.ontap.na_ontap_license
    na_ontap_lun:
      redirect: netapp.ontap.na_ontap_lun
    na_ontap_lun_copy:
      redirect: netapp.ontap.na_ontap_lun_copy
    na_ontap_lun_map:
      redirect: netapp.ontap.na_ontap_lun_map
    na_ontap_motd:
      redirect: netapp.ontap.na_ontap_motd
    na_ontap_ndmp:
      redirect: netapp.ontap.na_ontap_ndmp
    na_ontap_net_ifgrp:
      redirect: netapp.ontap.na_ontap_net_ifgrp
    na_ontap_net_port:
      redirect: netapp.ontap.na_ontap_net_port
    na_ontap_net_routes:
      redirect: netapp.ontap.na_ontap_net_routes
    na_ontap_net_subnet:
      redirect: netapp.ontap.na_ontap_net_subnet
    na_ontap_net_vlan:
      redirect: netapp.ontap.na_ontap_net_vlan
    na_ontap_nfs:
      redirect: netapp.ontap.na_ontap_nfs
    na_ontap_node:
      redirect: netapp.ontap.na_ontap_node
    na_ontap_ntp:
      redirect: netapp.ontap.na_ontap_ntp
    na_ontap_nvme:
      redirect: netapp.ontap.na_ontap_nvme
    na_ontap_nvme_namespace:
      redirect: netapp.ontap.na_ontap_nvme_namespace
    na_ontap_nvme_subsystem:
      redirect: netapp.ontap.na_ontap_nvme_subsystem
    na_ontap_object_store:
      redirect: netapp.ontap.na_ontap_object_store
    na_ontap_ports:
      redirect: netapp.ontap.na_ontap_ports
    na_ontap_portset:
      redirect: netapp.ontap.na_ontap_portset
    na_ontap_qos_adaptive_policy_group:
      redirect: netapp.ontap.na_ontap_qos_adaptive_policy_group
    na_ontap_qos_policy_group:
      redirect: netapp.ontap.na_ontap_qos_policy_group
    na_ontap_qtree:
      redirect: netapp.ontap.na_ontap_qtree
    na_ontap_quotas:
      redirect: netapp.ontap.na_ontap_quotas
    na_ontap_security_key_manager:
      redirect: netapp.ontap.na_ontap_security_key_manager
    na_ontap_service_processor_network:
      redirect: netapp.ontap.na_ontap_service_processor_network
    na_ontap_snapmirror:
      redirect: netapp.ontap.na_ontap_snapmirror
    na_ontap_snapshot:
      redirect: netapp.ontap.na_ontap_snapshot
    na_ontap_snapshot_policy:
      redirect: netapp.ontap.na_ontap_snapshot_policy
    na_ontap_snmp:
      redirect: netapp.ontap.na_ontap_snmp
    na_ontap_software_update:
      redirect: netapp.ontap.na_ontap_software_update
    na_ontap_svm:
      redirect: netapp.ontap.na_ontap_svm
    na_ontap_svm_options:
      redirect: netapp.ontap.na_ontap_svm_options
    na_ontap_ucadapter:
      redirect: netapp.ontap.na_ontap_ucadapter
    na_ontap_unix_group:
      redirect: netapp.ontap.na_ontap_unix_group
    na_ontap_unix_user:
      redirect: netapp.ontap.na_ontap_unix_user
    na_ontap_user:
      redirect: netapp.ontap.na_ontap_user
    na_ontap_user_role:
      redirect: netapp.ontap.na_ontap_user_role
    na_ontap_volume:
      redirect: netapp.ontap.na_ontap_volume
    na_ontap_volume_autosize:
      redirect: netapp.ontap.na_ontap_volume_autosize
    na_ontap_volume_clone:
      redirect: netapp.ontap.na_ontap_volume_clone
    na_ontap_vscan:
      redirect: netapp.ontap.na_ontap_vscan
    na_ontap_vscan_on_access_policy:
      redirect: netapp.ontap.na_ontap_vscan_on_access_policy
    na_ontap_vscan_on_demand_task:
      redirect: netapp.ontap.na_ontap_vscan_on_demand_task
    na_ontap_vscan_scanner_pool:
      redirect: netapp.ontap.na_ontap_vscan_scanner_pool
    na_ontap_vserver_cifs_security:
      redirect: netapp.ontap.na_ontap_vserver_cifs_security
    na_ontap_vserver_peer:
      redirect: netapp.ontap.na_ontap_vserver_peer
    cp_mgmt_access_layer:
      redirect: check_point.mgmt.cp_mgmt_access_layer
    cp_mgmt_access_layer_facts:
      redirect: check_point.mgmt.cp_mgmt_access_layer_facts
    cp_mgmt_access_role:
      redirect: check_point.mgmt.cp_mgmt_access_role
    cp_mgmt_access_role_facts:
      redirect: check_point.mgmt.cp_mgmt_access_role_facts
    cp_mgmt_access_rule:
      redirect: check_point.mgmt.cp_mgmt_access_rule
    cp_mgmt_access_rule_facts:
      redirect: check_point.mgmt.cp_mgmt_access_rule_facts
    cp_mgmt_address_range:
      redirect: check_point.mgmt.cp_mgmt_address_range
    cp_mgmt_address_range_facts:
      redirect: check_point.mgmt.cp_mgmt_address_range_facts
    cp_mgmt_administrator:
      redirect: check_point.mgmt.cp_mgmt_administrator
    cp_mgmt_administrator_facts:
      redirect: check_point.mgmt.cp_mgmt_administrator_facts
    cp_mgmt_application_site:
      redirect: check_point.mgmt.cp_mgmt_application_site
    cp_mgmt_application_site_category:
      redirect: check_point.mgmt.cp_mgmt_application_site_category
    cp_mgmt_application_site_category_facts:
      redirect: check_point.mgmt.cp_mgmt_application_site_category_facts
    cp_mgmt_application_site_facts:
      redirect: check_point.mgmt.cp_mgmt_application_site_facts
    cp_mgmt_application_site_group:
      redirect: check_point.mgmt.cp_mgmt_application_site_group
    cp_mgmt_application_site_group_facts:
      redirect: check_point.mgmt.cp_mgmt_application_site_group_facts
    cp_mgmt_assign_global_assignment:
      redirect: check_point.mgmt.cp_mgmt_assign_global_assignment
    cp_mgmt_discard:
      redirect: check_point.mgmt.cp_mgmt_discard
    cp_mgmt_dns_domain:
      redirect: check_point.mgmt.cp_mgmt_dns_domain
    cp_mgmt_dns_domain_facts:
      redirect: check_point.mgmt.cp_mgmt_dns_domain_facts
    cp_mgmt_dynamic_object:
      redirect: check_point.mgmt.cp_mgmt_dynamic_object
    cp_mgmt_dynamic_object_facts:
      redirect: check_point.mgmt.cp_mgmt_dynamic_object_facts
    cp_mgmt_exception_group:
      redirect: check_point.mgmt.cp_mgmt_exception_group
    cp_mgmt_exception_group_facts:
      redirect: check_point.mgmt.cp_mgmt_exception_group_facts
    cp_mgmt_global_assignment:
      redirect: check_point.mgmt.cp_mgmt_global_assignment
    cp_mgmt_global_assignment_facts:
      redirect: check_point.mgmt.cp_mgmt_global_assignment_facts
    cp_mgmt_group:
      redirect: check_point.mgmt.cp_mgmt_group
    cp_mgmt_group_facts:
      redirect: check_point.mgmt.cp_mgmt_group_facts
    cp_mgmt_group_with_exclusion:
      redirect: check_point.mgmt.cp_mgmt_group_with_exclusion
    cp_mgmt_group_with_exclusion_facts:
      redirect: check_point.mgmt.cp_mgmt_group_with_exclusion_facts
    cp_mgmt_host:
      redirect: check_point.mgmt.cp_mgmt_host
    cp_mgmt_host_facts:
      redirect: check_point.mgmt.cp_mgmt_host_facts
    cp_mgmt_install_policy:
      redirect: check_point.mgmt.cp_mgmt_install_policy
    cp_mgmt_mds_facts:
      redirect: check_point.mgmt.cp_mgmt_mds_facts
    cp_mgmt_multicast_address_range:
      redirect: check_point.mgmt.cp_mgmt_multicast_address_range
    cp_mgmt_multicast_address_range_facts:
      redirect: check_point.mgmt.cp_mgmt_multicast_address_range_facts
    cp_mgmt_network:
      redirect: check_point.mgmt.cp_mgmt_network
    cp_mgmt_network_facts:
      redirect: check_point.mgmt.cp_mgmt_network_facts
    cp_mgmt_package:
      redirect: check_point.mgmt.cp_mgmt_package
    cp_mgmt_package_facts:
      redirect: check_point.mgmt.cp_mgmt_package_facts
    cp_mgmt_publish:
      redirect: check_point.mgmt.cp_mgmt_publish
    cp_mgmt_put_file:
      redirect: check_point.mgmt.cp_mgmt_put_file
    cp_mgmt_run_ips_update:
      redirect: check_point.mgmt.cp_mgmt_run_ips_update
    cp_mgmt_run_script:
      redirect: check_point.mgmt.cp_mgmt_run_script
    cp_mgmt_security_zone:
      redirect: check_point.mgmt.cp_mgmt_security_zone
    cp_mgmt_security_zone_facts:
      redirect: check_point.mgmt.cp_mgmt_security_zone_facts
    cp_mgmt_service_dce_rpc:
      redirect: check_point.mgmt.cp_mgmt_service_dce_rpc
    cp_mgmt_service_dce_rpc_facts:
      redirect: check_point.mgmt.cp_mgmt_service_dce_rpc_facts
    cp_mgmt_service_group:
      redirect: check_point.mgmt.cp_mgmt_service_group
    cp_mgmt_service_group_facts:
      redirect: check_point.mgmt.cp_mgmt_service_group_facts
    cp_mgmt_service_icmp:
      redirect: check_point.mgmt.cp_mgmt_service_icmp
    cp_mgmt_service_icmp6:
      redirect: check_point.mgmt.cp_mgmt_service_icmp6
    cp_mgmt_service_icmp6_facts:
      redirect: check_point.mgmt.cp_mgmt_service_icmp6_facts
    cp_mgmt_service_icmp_facts:
      redirect: check_point.mgmt.cp_mgmt_service_icmp_facts
    cp_mgmt_service_other:
      redirect: check_point.mgmt.cp_mgmt_service_other
    cp_mgmt_service_other_facts:
      redirect: check_point.mgmt.cp_mgmt_service_other_facts
    cp_mgmt_service_rpc:
      redirect: check_point.mgmt.cp_mgmt_service_rpc
    cp_mgmt_service_rpc_facts:
      redirect: check_point.mgmt.cp_mgmt_service_rpc_facts
    cp_mgmt_service_sctp:
      redirect: check_point.mgmt.cp_mgmt_service_sctp
    cp_mgmt_service_sctp_facts:
      redirect: check_point.mgmt.cp_mgmt_service_sctp_facts
    cp_mgmt_service_tcp:
      redirect: check_point.mgmt.cp_mgmt_service_tcp
    cp_mgmt_service_tcp_facts:
      redirect: check_point.mgmt.cp_mgmt_service_tcp_facts
    cp_mgmt_service_udp:
      redirect: check_point.mgmt.cp_mgmt_service_udp
    cp_mgmt_service_udp_facts:
      redirect: check_point.mgmt.cp_mgmt_service_udp_facts
    cp_mgmt_session_facts:
      redirect: check_point.mgmt.cp_mgmt_session_facts
    cp_mgmt_simple_gateway:
      redirect: check_point.mgmt.cp_mgmt_simple_gateway
    cp_mgmt_simple_gateway_facts:
      redirect: check_point.mgmt.cp_mgmt_simple_gateway_facts
    cp_mgmt_tag:
      redirect: check_point.mgmt.cp_mgmt_tag
    cp_mgmt_tag_facts:
      redirect: check_point.mgmt.cp_mgmt_tag_facts
    cp_mgmt_threat_exception:
      redirect: check_point.mgmt.cp_mgmt_threat_exception
    cp_mgmt_threat_exception_facts:
      redirect: check_point.mgmt.cp_mgmt_threat_exception_facts
    cp_mgmt_threat_indicator:
      redirect: check_point.mgmt.cp_mgmt_threat_indicator
    cp_mgmt_threat_indicator_facts:
      redirect: check_point.mgmt.cp_mgmt_threat_indicator_facts
    cp_mgmt_threat_layer:
      redirect: check_point.mgmt.cp_mgmt_threat_layer
    cp_mgmt_threat_layer_facts:
      redirect: check_point.mgmt.cp_mgmt_threat_layer_facts
    cp_mgmt_threat_profile:
      redirect: check_point.mgmt.cp_mgmt_threat_profile
    cp_mgmt_threat_profile_facts:
      redirect: check_point.mgmt.cp_mgmt_threat_profile_facts
    cp_mgmt_threat_protection_override:
      redirect: check_point.mgmt.cp_mgmt_threat_protection_override
    cp_mgmt_threat_rule:
      redirect: check_point.mgmt.cp_mgmt_threat_rule
    cp_mgmt_threat_rule_facts:
      redirect: check_point.mgmt.cp_mgmt_threat_rule_facts
    cp_mgmt_time:
      redirect: check_point.mgmt.cp_mgmt_time
    cp_mgmt_time_facts:
      redirect: check_point.mgmt.cp_mgmt_time_facts
    cp_mgmt_verify_policy:
      redirect: check_point.mgmt.cp_mgmt_verify_policy
    cp_mgmt_vpn_community_meshed:
      redirect: check_point.mgmt.cp_mgmt_vpn_community_meshed
    cp_mgmt_vpn_community_meshed_facts:
      redirect: check_point.mgmt.cp_mgmt_vpn_community_meshed_facts
    cp_mgmt_vpn_community_star:
      redirect: check_point.mgmt.cp_mgmt_vpn_community_star
    cp_mgmt_vpn_community_star_facts:
      redirect: check_point.mgmt.cp_mgmt_vpn_community_star_facts
    cp_mgmt_wildcard:
      redirect: check_point.mgmt.cp_mgmt_wildcard
    cp_mgmt_wildcard_facts:
      redirect: check_point.mgmt.cp_mgmt_wildcard_facts
    eos_ospfv2:
      redirect: arista.eos.eos_ospfv2
    eos_static_route:
      redirect: arista.eos.eos_static_route
    eos_acls:
      redirect: arista.eos.eos_acls
    eos_interfaces:
      redirect: arista.eos.eos_interfaces
    eos_facts:
      redirect: arista.eos.eos_facts
    eos_logging:
      redirect: arista.eos.eos_logging
    eos_lag_interfaces:
      redirect: arista.eos.eos_lag_interfaces
    eos_l2_interfaces:
      redirect: arista.eos.eos_l2_interfaces
    eos_l3_interface:
      redirect: arista.eos.eos_l3_interface
    eos_lacp:
      redirect: arista.eos.eos_lacp
    eos_lldp_global:
      redirect: arista.eos.eos_lldp_global
    eos_static_routes:
      redirect: arista.eos.eos_static_routes
    eos_lacp_interfaces:
      redirect: arista.eos.eos_lacp_interfaces
    eos_system:
      redirect: arista.eos.eos_system
    eos_vlan:
      redirect: arista.eos.eos_vlan
    eos_eapi:
      redirect: arista.eos.eos_eapi
    eos_acl_interfaces:
      redirect: arista.eos.eos_acl_interfaces
    eos_l2_interface:
      redirect: arista.eos.eos_l2_interface
    eos_lldp_interfaces:
      redirect: arista.eos.eos_lldp_interfaces
    eos_command:
      redirect: arista.eos.eos_command
    eos_linkagg:
      redirect: arista.eos.eos_linkagg
    eos_l3_interfaces:
      redirect: arista.eos.eos_l3_interfaces
    eos_vlans:
      redirect: arista.eos.eos_vlans
    eos_user:
      redirect: arista.eos.eos_user
    eos_banner:
      redirect: arista.eos.eos_banner
    eos_lldp:
      redirect: arista.eos.eos_lldp
    eos_interface:
      redirect: arista.eos.eos_interface
    eos_config:
      redirect: arista.eos.eos_config
    eos_bgp:
      redirect: arista.eos.eos_bgp
    eos_vrf:
      redirect: arista.eos.eos_vrf
    aci_aaa_user:
      redirect: cisco.aci.aci_aaa_user
    aci_aaa_user_certificate:
      redirect: cisco.aci.aci_aaa_user_certificate
    aci_access_port_block_to_access_port:
      redirect: cisco.aci.aci_access_port_block_to_access_port
    aci_access_port_to_interface_policy_leaf_profile:
      redirect: cisco.aci.aci_access_port_to_interface_policy_leaf_profile
    aci_access_sub_port_block_to_access_port:
      redirect: cisco.aci.aci_access_sub_port_block_to_access_port
    aci_aep:
      redirect: cisco.aci.aci_aep
    aci_aep_to_domain:
      redirect: cisco.aci.aci_aep_to_domain
    aci_ap:
      redirect: cisco.aci.aci_ap
    aci_bd:
      redirect: cisco.aci.aci_bd
    aci_bd_subnet:
      redirect: cisco.aci.aci_bd_subnet
    aci_bd_to_l3out:
      redirect: cisco.aci.aci_bd_to_l3out
    aci_config_rollback:
      redirect: cisco.aci.aci_config_rollback
    aci_config_snapshot:
      redirect: cisco.aci.aci_config_snapshot
    aci_contract:
      redirect: cisco.aci.aci_contract
    aci_contract_subject:
      redirect: cisco.aci.aci_contract_subject
    aci_contract_subject_to_filter:
      redirect: cisco.aci.aci_contract_subject_to_filter
    aci_domain:
      redirect: cisco.aci.aci_domain
    aci_domain_to_encap_pool:
      redirect: cisco.aci.aci_domain_to_encap_pool
    aci_domain_to_vlan_pool:
      redirect: cisco.aci.aci_domain_to_vlan_pool
    aci_encap_pool:
      redirect: cisco.aci.aci_encap_pool
    aci_encap_pool_range:
      redirect: cisco.aci.aci_encap_pool_range
    aci_epg:
      redirect: cisco.aci.aci_epg
    aci_epg_monitoring_policy:
      redirect: cisco.aci.aci_epg_monitoring_policy
    aci_epg_to_contract:
      redirect: cisco.aci.aci_epg_to_contract
    aci_epg_to_domain:
      redirect: cisco.aci.aci_epg_to_domain
    aci_fabric_node:
      redirect: cisco.aci.aci_fabric_node
    aci_fabric_scheduler:
      redirect: cisco.aci.aci_fabric_scheduler
    aci_filter:
      redirect: cisco.aci.aci_filter
    aci_filter_entry:
      redirect: cisco.aci.aci_filter_entry
    aci_firmware_group:
      redirect: cisco.aci.aci_firmware_group
    aci_firmware_group_node:
      redirect: cisco.aci.aci_firmware_group_node
    aci_firmware_policy:
      redirect: cisco.aci.aci_firmware_policy
    aci_firmware_source:
      redirect: cisco.aci.aci_firmware_source
    aci_interface_policy_cdp:
      redirect: cisco.aci.aci_interface_policy_cdp
    aci_interface_policy_fc:
      redirect: cisco.aci.aci_interface_policy_fc
    aci_interface_policy_l2:
      redirect: cisco.aci.aci_interface_policy_l2
    aci_interface_policy_leaf_policy_group:
      redirect: cisco.aci.aci_interface_policy_leaf_policy_group
    aci_interface_policy_leaf_profile:
      redirect: cisco.aci.aci_interface_policy_leaf_profile
    aci_interface_policy_lldp:
      redirect: cisco.aci.aci_interface_policy_lldp
    aci_interface_policy_mcp:
      redirect: cisco.aci.aci_interface_policy_mcp
    aci_interface_policy_ospf:
      redirect: cisco.aci.aci_interface_policy_ospf
    aci_interface_policy_port_channel:
      redirect: cisco.aci.aci_interface_policy_port_channel
    aci_interface_policy_port_security:
      redirect: cisco.aci.aci_interface_policy_port_security
    aci_interface_selector_to_switch_policy_leaf_profile:
      redirect: cisco.aci.aci_interface_selector_to_switch_policy_leaf_profile
    aci_l3out:
      redirect: cisco.aci.aci_l3out
    aci_l3out_extepg:
      redirect: cisco.aci.aci_l3out_extepg
    aci_l3out_extsubnet:
      redirect: cisco.aci.aci_l3out_extsubnet
    aci_l3out_route_tag_policy:
      redirect: cisco.aci.aci_l3out_route_tag_policy
    aci_maintenance_group:
      redirect: cisco.aci.aci_maintenance_group
    aci_maintenance_group_node:
      redirect: cisco.aci.aci_maintenance_group_node
    aci_maintenance_policy:
      redirect: cisco.aci.aci_maintenance_policy
    aci_rest:
      redirect: cisco.aci.aci_rest
    aci_static_binding_to_epg:
      redirect: cisco.aci.aci_static_binding_to_epg
    aci_switch_leaf_selector:
      redirect: cisco.aci.aci_switch_leaf_selector
    aci_switch_policy_leaf_profile:
      redirect: cisco.aci.aci_switch_policy_leaf_profile
    aci_switch_policy_vpc_protection_group:
      redirect: cisco.aci.aci_switch_policy_vpc_protection_group
    aci_taboo_contract:
      redirect: cisco.aci.aci_taboo_contract
    aci_tenant:
      redirect: cisco.aci.aci_tenant
    aci_tenant_action_rule_profile:
      redirect: cisco.aci.aci_tenant_action_rule_profile
    aci_tenant_ep_retention_policy:
      redirect: cisco.aci.aci_tenant_ep_retention_policy
    aci_tenant_span_dst_group:
      redirect: cisco.aci.aci_tenant_span_dst_group
    aci_tenant_span_src_group:
      redirect: cisco.aci.aci_tenant_span_src_group
    aci_tenant_span_src_group_to_dst_group:
      redirect: cisco.aci.aci_tenant_span_src_group_to_dst_group
    aci_vlan_pool:
      redirect: cisco.aci.aci_vlan_pool
    aci_vlan_pool_encap_block:
      redirect: cisco.aci.aci_vlan_pool_encap_block
    aci_vmm_credential:
      redirect: cisco.aci.aci_vmm_credential
    aci_vrf:
      redirect: cisco.aci.aci_vrf
    asa_acl:
      redirect: cisco.asa.asa_acl
    asa_config:
      redirect: cisco.asa.asa_config
    asa_og:
      redirect: cisco.asa.asa_og
    asa_command:
      redirect: cisco.asa.asa_command
    intersight_facts:
      redirect: cisco.intersight.intersight_info
    intersight_info:
      redirect: cisco.intersight.intersight_info
    intersight_rest_api:
      redirect: cisco.intersight.intersight_rest_api
    ios_ospfv2:
      redirect: cisco.ios.ios_ospfv2
    ios_l3_interfaces:
      redirect: cisco.ios.ios_l3_interfaces
    ios_lldp:
      redirect: cisco.ios.ios_lldp
    ios_interface:
      redirect: cisco.ios.ios_interface
    ios_lldp_interfaces:
      redirect: cisco.ios.ios_lldp_interfaces
    ios_l3_interface:
      redirect: cisco.ios.ios_l3_interface
    ios_acl_interfaces:
      redirect: cisco.ios.ios_acl_interfaces
    ios_static_routes:
      redirect: cisco.ios.ios_static_routes
    ios_l2_interfaces:
      redirect: cisco.ios.ios_l2_interfaces
    ios_logging:
      redirect: cisco.ios.ios_logging
    ios_vlan:
      redirect: cisco.ios.ios_vlan
    ios_command:
      redirect: cisco.ios.ios_command
    ios_static_route:
      redirect: cisco.ios.ios_static_route
    ios_lldp_global:
      redirect: cisco.ios.ios_lldp_global
    ios_banner:
      redirect: cisco.ios.ios_banner
    ios_lag_interfaces:
      redirect: cisco.ios.ios_lag_interfaces
    ios_linkagg:
      redirect: cisco.ios.ios_linkagg
    ios_user:
      redirect: cisco.ios.ios_user
    ios_system:
      redirect: cisco.ios.ios_system
    ios_facts:
      redirect: cisco.ios.ios_facts
    ios_ping:
      redirect: cisco.ios.ios_ping
    ios_vlans:
      redirect: cisco.ios.ios_vlans
    ios_vrf:
      redirect: cisco.ios.ios_vrf
    ios_bgp:
      redirect: cisco.ios.ios_bgp
    ios_ntp:
      redirect: cisco.ios.ios_ntp
    ios_lacp_interfaces:
      redirect: cisco.ios.ios_lacp_interfaces
    ios_lacp:
      redirect: cisco.ios.ios_lacp
    ios_config:
      redirect: cisco.ios.ios_config
    ios_l2_interface:
      redirect: cisco.ios.ios_l2_interface
    ios_acls:
      redirect: cisco.ios.ios_acls
    ios_interfaces:
      redirect: cisco.ios.ios_interfaces
    iosxr_ospfv2:
      redirect: cisco.iosxr.iosxr_ospfv2
    iosxr_bgp:
      redirect: cisco.iosxr.iosxr_bgp
    iosxr_lldp_interfaces:
      redirect: cisco.iosxr.iosxr_lldp_interfaces
    iosxr_l3_interfaces:
      redirect: cisco.iosxr.iosxr_l3_interfaces
    iosxr_netconf:
      redirect: cisco.iosxr.iosxr_netconf
    iosxr_static_routes:
      redirect: cisco.iosxr.iosxr_static_routes
    iosxr_lldp_global:
      redirect: cisco.iosxr.iosxr_lldp_global
    iosxr_config:
      redirect: cisco.iosxr.iosxr_config
    iosxr_lag_interfaces:
      redirect: cisco.iosxr.iosxr_lag_interfaces
    iosxr_interface:
      redirect: cisco.iosxr.iosxr_interface
    iosxr_user:
      redirect: cisco.iosxr.iosxr_user
    iosxr_facts:
      redirect: cisco.iosxr.iosxr_facts
    iosxr_interfaces:
      redirect: cisco.iosxr.iosxr_interfaces
    iosxr_acl_interfaces:
      redirect: cisco.iosxr.iosxr_acl_interfaces
    iosxr_l2_interfaces:
      redirect: cisco.iosxr.iosxr_l2_interfaces
    iosxr_logging:
      redirect: cisco.iosxr.iosxr_logging
    iosxr_lacp:
      redirect: cisco.iosxr.iosxr_lacp
    iosxr_acls:
      redirect: cisco.iosxr.iosxr_acls
    iosxr_system:
      redirect: cisco.iosxr.iosxr_system
    iosxr_command:
      redirect: cisco.iosxr.iosxr_command
    iosxr_lacp_interfaces:
      redirect: cisco.iosxr.iosxr_lacp_interfaces
    iosxr_banner:
      redirect: cisco.iosxr.iosxr_banner
    meraki_admin:
      redirect: cisco.meraki.meraki_admin
    meraki_config_template:
      redirect: cisco.meraki.meraki_config_template
    meraki_content_filtering:
      redirect: cisco.meraki.meraki_content_filtering
    meraki_device:
      redirect: cisco.meraki.meraki_device
    meraki_firewalled_services:
      redirect: cisco.meraki.meraki_firewalled_services
    meraki_malware:
      redirect: cisco.meraki.meraki_malware
    meraki_mr_l3_firewall:
      redirect: cisco.meraki.meraki_mr_l3_firewall
    meraki_mx_l3_firewall:
      redirect: cisco.meraki.meraki_mx_l3_firewall
    meraki_mx_l7_firewall:
      redirect: cisco.meraki.meraki_mx_l7_firewall
    meraki_nat:
      redirect: cisco.meraki.meraki_nat
    meraki_network:
      redirect: cisco.meraki.meraki_network
    meraki_organization:
      redirect: cisco.meraki.meraki_organization
    meraki_snmp:
      redirect: cisco.meraki.meraki_snmp
    meraki_ssid:
      redirect: cisco.meraki.meraki_ssid
    meraki_static_route:
      redirect: cisco.meraki.meraki_static_route
    meraki_switchport:
      redirect: cisco.meraki.meraki_switchport
    meraki_syslog:
      redirect: cisco.meraki.meraki_syslog
    meraki_vlan:
      redirect: cisco.meraki.meraki_vlan
    meraki_webhook:
      redirect: cisco.meraki.meraki_webhook
    mso_label:
      redirect: cisco.mso.mso_label
    mso_role:
      redirect: cisco.mso.mso_role
    mso_schema:
      redirect: cisco.mso.mso_schema
    mso_schema_site:
      redirect: cisco.mso.mso_schema_site
    mso_schema_site_anp:
      redirect: cisco.mso.mso_schema_site_anp
    mso_schema_site_anp_epg:
      redirect: cisco.mso.mso_schema_site_anp_epg
    mso_schema_site_anp_epg_domain:
      redirect: cisco.mso.mso_schema_site_anp_epg_domain
    mso_schema_site_anp_epg_staticleaf:
      redirect: cisco.mso.mso_schema_site_anp_epg_staticleaf
    mso_schema_site_anp_epg_staticport:
      redirect: cisco.mso.mso_schema_site_anp_epg_staticport
    mso_schema_site_anp_epg_subnet:
      redirect: cisco.mso.mso_schema_site_anp_epg_subnet
    mso_schema_site_bd:
      redirect: cisco.mso.mso_schema_site_bd
    mso_schema_site_bd_l3out:
      redirect: cisco.mso.mso_schema_site_bd_l3out
    mso_schema_site_bd_subnet:
      redirect: cisco.mso.mso_schema_site_bd_subnet
    mso_schema_site_vrf:
      redirect: cisco.mso.mso_schema_site_vrf
    mso_schema_site_vrf_region:
      redirect: cisco.mso.mso_schema_site_vrf_region
    mso_schema_site_vrf_region_cidr:
      redirect: cisco.mso.mso_schema_site_vrf_region_cidr
    mso_schema_site_vrf_region_cidr_subnet:
      redirect: cisco.mso.mso_schema_site_vrf_region_cidr_subnet
    mso_schema_template:
      redirect: cisco.mso.mso_schema_template
    mso_schema_template_anp:
      redirect: cisco.mso.mso_schema_template_anp
    mso_schema_template_anp_epg:
      redirect: cisco.mso.mso_schema_template_anp_epg
    mso_schema_template_anp_epg_contract:
      redirect: cisco.mso.mso_schema_template_anp_epg_contract
    mso_schema_template_anp_epg_subnet:
      redirect: cisco.mso.mso_schema_template_anp_epg_subnet
    mso_schema_template_bd:
      redirect: cisco.mso.mso_schema_template_bd
    mso_schema_template_bd_subnet:
      redirect: cisco.mso.mso_schema_template_bd_subnet
    mso_schema_template_contract_filter:
      redirect: cisco.mso.mso_schema_template_contract_filter
    mso_schema_template_deploy:
      redirect: cisco.mso.mso_schema_template_deploy
    mso_schema_template_externalepg:
      redirect: cisco.mso.mso_schema_template_externalepg
    mso_schema_template_filter_entry:
      redirect: cisco.mso.mso_schema_template_filter_entry
    mso_schema_template_l3out:
      redirect: cisco.mso.mso_schema_template_l3out
    mso_schema_template_vrf:
      redirect: cisco.mso.mso_schema_template_vrf
    mso_site:
      redirect: cisco.mso.mso_site
    mso_tenant:
      redirect: cisco.mso.mso_tenant
    mso_user:
      redirect: cisco.mso.mso_user
    nxos_telemetry:
      redirect: cisco.nxos.nxos_telemetry
    nxos_user:
      redirect: cisco.nxos.nxos_user
    nxos_bfd_interfaces:
      redirect: cisco.nxos.nxos_bfd_interfaces
    nxos_ospf:
      redirect: cisco.nxos.nxos_ospf
    nxos_ospfv2:
      redirect: cisco.nxos.nxos_ospfv2
    nxos_system:
      redirect: cisco.nxos.nxos_system
    nxos_l3_interface:
      redirect: cisco.nxos.nxos_l3_interface
    nxos_smu:
      redirect: cisco.nxos.nxos_smu
    nxos_reboot:
      redirect: cisco.nxos.nxos_reboot
    nxos_static_routes:
      redirect: cisco.nxos.nxos_static_routes
    nxos_static_route:
      redirect: cisco.nxos.nxos_static_route
    nxos_acl_interfaces:
      redirect: cisco.nxos.nxos_acl_interfaces
    nxos_vpc:
      redirect: cisco.nxos.nxos_vpc
    nxos_linkagg:
      redirect: cisco.nxos.nxos_linkagg
    nxos_vxlan_vtep_vni:
      redirect: cisco.nxos.nxos_vxlan_vtep_vni
    nxos_vrrp:
      redirect: cisco.nxos.nxos_vrrp
    nxos_lldp:
      redirect: cisco.nxos.nxos_lldp
    nxos_interface:
      redirect: cisco.nxos.nxos_interface
    nxos_lacp_interfaces:
      redirect: cisco.nxos.nxos_lacp_interfaces
    nxos_gir_profile_management:
      redirect: cisco.nxos.nxos_gir_profile_management
    nxos_snmp_community:
      redirect: cisco.nxos.nxos_snmp_community
    nxos_lag_interfaces:
      redirect: cisco.nxos.nxos_lag_interfaces
    nxos_acl:
      redirect: cisco.nxos.nxos_acl
    nxos_hsrp_interfaces:
      redirect: cisco.nxos.nxos_hsrp_interfaces
    nxos_lldp_global:
      redirect: cisco.nxos.nxos_lldp_global
    nxos_snmp_contact:
      redirect: cisco.nxos.nxos_snmp_contact
    nxos_vrf_interface:
      redirect: cisco.nxos.nxos_vrf_interface
    nxos_rpm:
      redirect: cisco.nxos.nxos_rpm
    nxos_ntp_options:
      redirect: cisco.nxos.nxos_ntp_options
    nxos_ospf_vrf:
      redirect: cisco.nxos.nxos_ospf_vrf
    nxos_vtp_version:
      redirect: cisco.nxos.nxos_vtp_version
    nxos_igmp_interface:
      redirect: cisco.nxos.nxos_igmp_interface
    nxos_bgp_neighbor:
      redirect: cisco.nxos.nxos_bgp_neighbor
    nxos_bgp:
      redirect: cisco.nxos.nxos_bgp
    nxos_rollback:
      redirect: cisco.nxos.nxos_rollback
    nxos_aaa_server:
      redirect: cisco.nxos.nxos_aaa_server
    nxos_udld_interface:
      redirect: cisco.nxos.nxos_udld_interface
    nxos_bgp_af:
      redirect: cisco.nxos.nxos_bgp_af
    nxos_feature:
      redirect: cisco.nxos.nxos_feature
    nxos_snmp_traps:
      redirect: cisco.nxos.nxos_snmp_traps
    nxos_evpn_global:
      redirect: cisco.nxos.nxos_evpn_global
    nxos_igmp:
      redirect: cisco.nxos.nxos_igmp
    nxos_aaa_server_host:
      redirect: cisco.nxos.nxos_aaa_server_host
    nxos_vrf_af:
      redirect: cisco.nxos.nxos_vrf_af
    nxos_snapshot:
      redirect: cisco.nxos.nxos_snapshot
    nxos_gir:
      redirect: cisco.nxos.nxos_gir
    nxos_command:
      redirect: cisco.nxos.nxos_command
    nxos_vxlan_vtep:
      redirect: cisco.nxos.nxos_vxlan_vtep
    nxos_snmp_location:
      redirect: cisco.nxos.nxos_snmp_location
    nxos_evpn_vni:
      redirect: cisco.nxos.nxos_evpn_vni
    nxos_vpc_interface:
      redirect: cisco.nxos.nxos_vpc_interface
    nxos_logging:
      redirect: cisco.nxos.nxos_logging
    nxos_pim:
      redirect: cisco.nxos.nxos_pim
    nxos_ping:
      redirect: cisco.nxos.nxos_ping
    nxos_pim_rp_address:
      redirect: cisco.nxos.nxos_pim_rp_address
    nxos_pim_interface:
      redirect: cisco.nxos.nxos_pim_interface
    nxos_install_os:
      redirect: cisco.nxos.nxos_install_os
    nxos_nxapi:
      redirect: cisco.nxos.nxos_nxapi
    nxos_l2_interface:
      redirect: cisco.nxos.nxos_l2_interface
    nxos_bgp_neighbor_af:
      redirect: cisco.nxos.nxos_bgp_neighbor_af
    nxos_lacp:
      redirect: cisco.nxos.nxos_lacp
    nxos_lldp_interfaces:
      redirect: cisco.nxos.nxos_lldp_interfaces
    nxos_acl_interface:
      redirect: cisco.nxos.nxos_acl_interface
    nxos_vrf:
      redirect: cisco.nxos.nxos_vrf
    nxos_interface_ospf:
      redirect: cisco.nxos.nxos_interface_ospf
    nxos_acls:
      redirect: cisco.nxos.nxos_acls
    nxos_vtp_password:
      redirect: cisco.nxos.nxos_vtp_password
    nxos_l3_interfaces:
      redirect: cisco.nxos.nxos_l3_interfaces
    nxos_igmp_snooping:
      redirect: cisco.nxos.nxos_igmp_snooping
    nxos_banner:
      redirect: cisco.nxos.nxos_banner
    nxos_bfd_global:
      redirect: cisco.nxos.nxos_bfd_global
    nxos_udld:
      redirect: cisco.nxos.nxos_udld
    nxos_vtp_domain:
      redirect: cisco.nxos.nxos_vtp_domain
    nxos_snmp_host:
      redirect: cisco.nxos.nxos_snmp_host
    nxos_l2_interfaces:
      redirect: cisco.nxos.nxos_l2_interfaces
    nxos_hsrp:
      redirect: cisco.nxos.nxos_hsrp
    nxos_interfaces:
      redirect: cisco.nxos.nxos_interfaces
    nxos_overlay_global:
      redirect: cisco.nxos.nxos_overlay_global
    nxos_snmp_user:
      redirect: cisco.nxos.nxos_snmp_user
    nxos_vlans:
      redirect: cisco.nxos.nxos_vlans
    nxos_ntp:
      redirect: cisco.nxos.nxos_ntp
    nxos_file_copy:
      redirect: cisco.nxos.nxos_file_copy
    nxos_ntp_auth:
      redirect: cisco.nxos.nxos_ntp_auth
    nxos_config:
      redirect: cisco.nxos.nxos_config
    nxos_vlan:
      redirect: cisco.nxos.nxos_vlan
    nxos_facts:
      redirect: cisco.nxos.nxos_facts
    nxos_zone_zoneset:
      redirect: cisco.nxos.nxos_zone_zoneset
    nxos_vsan:
      redirect: cisco.nxos.nxos_vsan
    nxos_devicealias:
      redirect: cisco.nxos.nxos_devicealias
    ucs_managed_objects:
      redirect: cisco.ucs.ucs_managed_objects
    ucs_vnic_template:
      redirect: cisco.ucs.ucs_vnic_template
    ucs_query:
      redirect: cisco.ucs.ucs_query
    ucs_dns_server:
      redirect: cisco.ucs.ucs_dns_server
    ucs_lan_connectivity:
      redirect: cisco.ucs.ucs_lan_connectivity
    ucs_vhba_template:
      redirect: cisco.ucs.ucs_vhba_template
    ucs_san_connectivity:
      redirect: cisco.ucs.ucs_san_connectivity
    ucs_disk_group_policy:
      redirect: cisco.ucs.ucs_disk_group_policy
    ucs_uuid_pool:
      redirect: cisco.ucs.ucs_uuid_pool
    ucs_vlan_find:
      redirect: cisco.ucs.ucs_vlan_find
    ucs_vlans:
      redirect: cisco.ucs.ucs_vlans
    ucs_service_profile_template:
      redirect: cisco.ucs.ucs_service_profile_template
    ucs_ip_pool:
      redirect: cisco.ucs.ucs_ip_pool
    ucs_timezone:
      redirect: cisco.ucs.ucs_timezone
    ucs_ntp_server:
      redirect: cisco.ucs.ucs_ntp_server
    ucs_mac_pool:
      redirect: cisco.ucs.ucs_mac_pool
    ucs_storage_profile:
      redirect: cisco.ucs.ucs_storage_profile
    ucs_org:
      redirect: cisco.ucs.ucs_org
    ucs_vsans:
      redirect: cisco.ucs.ucs_vsans
    ucs_wwn_pool:
      redirect: cisco.ucs.ucs_wwn_pool
    bigip_apm_acl:
      redirect: f5networks.f5_modules.bigip_apm_acl
    bigip_apm_network_access:
      redirect: f5networks.f5_modules.bigip_apm_network_access
    bigip_apm_policy_fetch:
      redirect: f5networks.f5_modules.bigip_apm_policy_fetch
    bigip_apm_policy_import:
      redirect: f5networks.f5_modules.bigip_apm_policy_import
    bigip_appsvcs_extension:
      redirect: f5networks.f5_modules.bigip_appsvcs_extension
    bigip_asm_dos_application:
      redirect: f5networks.f5_modules.bigip_asm_dos_application
    bigip_asm_policy_fetch:
      redirect: f5networks.f5_modules.bigip_asm_policy_fetch
    bigip_asm_policy_import:
      redirect: f5networks.f5_modules.bigip_asm_policy_import
    bigip_asm_policy_manage:
      redirect: f5networks.f5_modules.bigip_asm_policy_manage
    bigip_asm_policy_server_technology:
      redirect: f5networks.f5_modules.bigip_asm_policy_server_technology
    bigip_asm_policy_signature_set:
      redirect: f5networks.f5_modules.bigip_asm_policy_signature_set
    bigip_cli_alias:
      redirect: f5networks.f5_modules.bigip_cli_alias
    bigip_cli_script:
      redirect: f5networks.f5_modules.bigip_cli_script
    bigip_command:
      redirect: f5networks.f5_modules.bigip_command
    bigip_config:
      redirect: f5networks.f5_modules.bigip_config
    bigip_configsync_action:
      redirect: f5networks.f5_modules.bigip_configsync_action
    bigip_data_group:
      redirect: f5networks.f5_modules.bigip_data_group
    bigip_device_auth:
      redirect: f5networks.f5_modules.bigip_device_auth
    bigip_device_auth_ldap:
      redirect: f5networks.f5_modules.bigip_device_auth_ldap
    bigip_device_certificate:
      redirect: f5networks.f5_modules.bigip_device_certificate
    bigip_device_connectivity:
      redirect: f5networks.f5_modules.bigip_device_connectivity
    bigip_device_dns:
      redirect: f5networks.f5_modules.bigip_device_dns
    bigip_device_group:
      redirect: f5networks.f5_modules.bigip_device_group
    bigip_device_group_member:
      redirect: f5networks.f5_modules.bigip_device_group_member
    bigip_device_ha_group:
      redirect: f5networks.f5_modules.bigip_device_ha_group
    bigip_device_httpd:
      redirect: f5networks.f5_modules.bigip_device_httpd
    bigip_device_info:
      redirect: f5networks.f5_modules.bigip_device_info
    bigip_device_license:
      redirect: f5networks.f5_modules.bigip_device_license
    bigip_device_ntp:
      redirect: f5networks.f5_modules.bigip_device_ntp
    bigip_device_sshd:
      redirect: f5networks.f5_modules.bigip_device_sshd
    bigip_device_syslog:
      redirect: f5networks.f5_modules.bigip_device_syslog
    bigip_device_traffic_group:
      redirect: f5networks.f5_modules.bigip_device_traffic_group
    bigip_device_trust:
      redirect: f5networks.f5_modules.bigip_device_trust
    bigip_dns_cache_resolver:
      redirect: f5networks.f5_modules.bigip_dns_cache_resolver
    bigip_dns_nameserver:
      redirect: f5networks.f5_modules.bigip_dns_nameserver
    bigip_dns_resolver:
      redirect: f5networks.f5_modules.bigip_dns_resolver
    bigip_dns_zone:
      redirect: f5networks.f5_modules.bigip_dns_zone
    bigip_file_copy:
      redirect: f5networks.f5_modules.bigip_file_copy
    bigip_firewall_address_list:
      redirect: f5networks.f5_modules.bigip_firewall_address_list
    bigip_firewall_dos_profile:
      redirect: f5networks.f5_modules.bigip_firewall_dos_profile
    bigip_firewall_dos_vector:
      redirect: f5networks.f5_modules.bigip_firewall_dos_vector
    bigip_firewall_global_rules:
      redirect: f5networks.f5_modules.bigip_firewall_global_rules
    bigip_firewall_log_profile:
      redirect: f5networks.f5_modules.bigip_firewall_log_profile
    bigip_firewall_log_profile_network:
      redirect: f5networks.f5_modules.bigip_firewall_log_profile_network
    bigip_firewall_policy:
      redirect: f5networks.f5_modules.bigip_firewall_policy
    bigip_firewall_port_list:
      redirect: f5networks.f5_modules.bigip_firewall_port_list
    bigip_firewall_rule:
      redirect: f5networks.f5_modules.bigip_firewall_rule
    bigip_firewall_rule_list:
      redirect: f5networks.f5_modules.bigip_firewall_rule_list
    bigip_firewall_schedule:
      redirect: f5networks.f5_modules.bigip_firewall_schedule
    bigip_gtm_datacenter:
      redirect: f5networks.f5_modules.bigip_gtm_datacenter
    bigip_gtm_global:
      redirect: f5networks.f5_modules.bigip_gtm_global
    bigip_gtm_monitor_bigip:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_bigip
    bigip_gtm_monitor_external:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_external
    bigip_gtm_monitor_firepass:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_firepass
    bigip_gtm_monitor_http:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_http
    bigip_gtm_monitor_https:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_https
    bigip_gtm_monitor_tcp:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_tcp
    bigip_gtm_monitor_tcp_half_open:
      redirect: f5networks.f5_modules.bigip_gtm_monitor_tcp_half_open
    bigip_gtm_pool:
      redirect: f5networks.f5_modules.bigip_gtm_pool
    bigip_gtm_pool_member:
      redirect: f5networks.f5_modules.bigip_gtm_pool_member
    bigip_gtm_server:
      redirect: f5networks.f5_modules.bigip_gtm_server
    bigip_gtm_topology_record:
      redirect: f5networks.f5_modules.bigip_gtm_topology_record
    bigip_gtm_topology_region:
      redirect: f5networks.f5_modules.bigip_gtm_topology_region
    bigip_gtm_virtual_server:
      redirect: f5networks.f5_modules.bigip_gtm_virtual_server
    bigip_gtm_wide_ip:
      redirect: f5networks.f5_modules.bigip_gtm_wide_ip
    bigip_hostname:
      redirect: f5networks.f5_modules.bigip_hostname
    bigip_iapp_service:
      redirect: f5networks.f5_modules.bigip_iapp_service
    bigip_iapp_template:
      redirect: f5networks.f5_modules.bigip_iapp_template
    bigip_ike_peer:
      redirect: f5networks.f5_modules.bigip_ike_peer
    bigip_imish_config:
      redirect: f5networks.f5_modules.bigip_imish_config
    bigip_ipsec_policy:
      redirect: f5networks.f5_modules.bigip_ipsec_policy
    bigip_irule:
      redirect: f5networks.f5_modules.bigip_irule
    bigip_log_destination:
      redirect: f5networks.f5_modules.bigip_log_destination
    bigip_log_publisher:
      redirect: f5networks.f5_modules.bigip_log_publisher
    bigip_lx_package:
      redirect: f5networks.f5_modules.bigip_lx_package
    bigip_management_route:
      redirect: f5networks.f5_modules.bigip_management_route
    bigip_message_routing_peer:
      redirect: f5networks.f5_modules.bigip_message_routing_peer
    bigip_message_routing_protocol:
      redirect: f5networks.f5_modules.bigip_message_routing_protocol
    bigip_message_routing_route:
      redirect: f5networks.f5_modules.bigip_message_routing_route
    bigip_message_routing_router:
      redirect: f5networks.f5_modules.bigip_message_routing_router
    bigip_message_routing_transport_config:
      redirect: f5networks.f5_modules.bigip_message_routing_transport_config
    bigip_monitor_dns:
      redirect: f5networks.f5_modules.bigip_monitor_dns
    bigip_monitor_external:
      redirect: f5networks.f5_modules.bigip_monitor_external
    bigip_monitor_gateway_icmp:
      redirect: f5networks.f5_modules.bigip_monitor_gateway_icmp
    bigip_monitor_http:
      redirect: f5networks.f5_modules.bigip_monitor_http
    bigip_monitor_https:
      redirect: f5networks.f5_modules.bigip_monitor_https
    bigip_monitor_ldap:
      redirect: f5networks.f5_modules.bigip_monitor_ldap
    bigip_monitor_snmp_dca:
      redirect: f5networks.f5_modules.bigip_monitor_snmp_dca
    bigip_monitor_tcp:
      redirect: f5networks.f5_modules.bigip_monitor_tcp
    bigip_monitor_tcp_echo:
      redirect: f5networks.f5_modules.bigip_monitor_tcp_echo
    bigip_monitor_tcp_half_open:
      redirect: f5networks.f5_modules.bigip_monitor_tcp_half_open
    bigip_monitor_udp:
      redirect: f5networks.f5_modules.bigip_monitor_udp
    bigip_node:
      redirect: f5networks.f5_modules.bigip_node
    bigip_partition:
      redirect: f5networks.f5_modules.bigip_partition
    bigip_password_policy:
      redirect: f5networks.f5_modules.bigip_password_policy
    bigip_policy:
      redirect: f5networks.f5_modules.bigip_policy
    bigip_policy_rule:
      redirect: f5networks.f5_modules.bigip_policy_rule
    bigip_pool:
      redirect: f5networks.f5_modules.bigip_pool
    bigip_pool_member:
      redirect: f5networks.f5_modules.bigip_pool_member
    bigip_profile_analytics:
      redirect: f5networks.f5_modules.bigip_profile_analytics
    bigip_profile_client_ssl:
      redirect: f5networks.f5_modules.bigip_profile_client_ssl
    bigip_profile_dns:
      redirect: f5networks.f5_modules.bigip_profile_dns
    bigip_profile_fastl4:
      redirect: f5networks.f5_modules.bigip_profile_fastl4
    bigip_profile_http:
      redirect: f5networks.f5_modules.bigip_profile_http
    bigip_profile_http2:
      redirect: f5networks.f5_modules.bigip_profile_http2
    bigip_profile_http_compression:
      redirect: f5networks.f5_modules.bigip_profile_http_compression
    bigip_profile_oneconnect:
      redirect: f5networks.f5_modules.bigip_profile_oneconnect
    bigip_profile_persistence_cookie:
      redirect: f5networks.f5_modules.bigip_profile_persistence_cookie
    bigip_profile_persistence_src_addr:
      redirect: f5networks.f5_modules.bigip_profile_persistence_src_addr
    bigip_profile_server_ssl:
      redirect: f5networks.f5_modules.bigip_profile_server_ssl
    bigip_profile_tcp:
      redirect: f5networks.f5_modules.bigip_profile_tcp
    bigip_profile_udp:
      redirect: f5networks.f5_modules.bigip_profile_udp
    bigip_provision:
      redirect: f5networks.f5_modules.bigip_provision
    bigip_qkview:
      redirect: f5networks.f5_modules.bigip_qkview
    bigip_remote_role:
      redirect: f5networks.f5_modules.bigip_remote_role
    bigip_remote_syslog:
      redirect: f5networks.f5_modules.bigip_remote_syslog
    bigip_remote_user:
      redirect: f5networks.f5_modules.bigip_remote_user
    bigip_routedomain:
      redirect: f5networks.f5_modules.bigip_routedomain
    bigip_selfip:
      redirect: f5networks.f5_modules.bigip_selfip
    bigip_service_policy:
      redirect: f5networks.f5_modules.bigip_service_policy
    bigip_smtp:
      redirect: f5networks.f5_modules.bigip_smtp
    bigip_snat_pool:
      redirect: f5networks.f5_modules.bigip_snat_pool
    bigip_snat_translation:
      redirect: f5networks.f5_modules.bigip_snat_translation
    bigip_snmp:
      redirect: f5networks.f5_modules.bigip_snmp
    bigip_snmp_community:
      redirect: f5networks.f5_modules.bigip_snmp_community
    bigip_snmp_trap:
      redirect: f5networks.f5_modules.bigip_snmp_trap
    bigip_software_image:
      redirect: f5networks.f5_modules.bigip_software_image
    bigip_software_install:
      redirect: f5networks.f5_modules.bigip_software_install
    bigip_software_update:
      redirect: f5networks.f5_modules.bigip_software_update
    bigip_ssl_certificate:
      redirect: f5networks.f5_modules.bigip_ssl_certificate
    bigip_ssl_key:
      redirect: f5networks.f5_modules.bigip_ssl_key
    bigip_ssl_ocsp:
      redirect: f5networks.f5_modules.bigip_ssl_ocsp
    bigip_static_route:
      redirect: f5networks.f5_modules.bigip_static_route
    bigip_sys_daemon_log_tmm:
      redirect: f5networks.f5_modules.bigip_sys_daemon_log_tmm
    bigip_sys_db:
      redirect: f5networks.f5_modules.bigip_sys_db
    bigip_sys_global:
      redirect: f5networks.f5_modules.bigip_sys_global
    bigip_timer_policy:
      redirect: f5networks.f5_modules.bigip_timer_policy
    bigip_traffic_selector:
      redirect: f5networks.f5_modules.bigip_traffic_selector
    bigip_trunk:
      redirect: f5networks.f5_modules.bigip_trunk
    bigip_tunnel:
      redirect: f5networks.f5_modules.bigip_tunnel
    bigip_ucs:
      redirect: f5networks.f5_modules.bigip_ucs
    bigip_ucs_fetch:
      redirect: f5networks.f5_modules.bigip_ucs_fetch
    bigip_user:
      redirect: f5networks.f5_modules.bigip_user
    bigip_vcmp_guest:
      redirect: f5networks.f5_modules.bigip_vcmp_guest
    bigip_virtual_address:
      redirect: f5networks.f5_modules.bigip_virtual_address
    bigip_virtual_server:
      redirect: f5networks.f5_modules.bigip_virtual_server
    bigip_vlan:
      redirect: f5networks.f5_modules.bigip_vlan
    bigip_wait:
      redirect: f5networks.f5_modules.bigip_wait
    bigiq_application_fasthttp:
      redirect: f5networks.f5_modules.bigiq_application_fasthttp
    bigiq_application_fastl4_tcp:
      redirect: f5networks.f5_modules.bigiq_application_fastl4_tcp
    bigiq_application_fastl4_udp:
      redirect: f5networks.f5_modules.bigiq_application_fastl4_udp
    bigiq_application_http:
      redirect: f5networks.f5_modules.bigiq_application_http
    bigiq_application_https_offload:
      redirect: f5networks.f5_modules.bigiq_application_https_offload
    bigiq_application_https_waf:
      redirect: f5networks.f5_modules.bigiq_application_https_waf
    bigiq_device_discovery:
      redirect: f5networks.f5_modules.bigiq_device_discovery
    bigiq_device_info:
      redirect: f5networks.f5_modules.bigiq_device_info
    bigiq_regkey_license:
      redirect: f5networks.f5_modules.bigiq_regkey_license
    bigiq_regkey_license_assignment:
      redirect: f5networks.f5_modules.bigiq_regkey_license_assignment
    bigiq_regkey_pool:
      redirect: f5networks.f5_modules.bigiq_regkey_pool
    bigiq_utility_license:
      redirect: f5networks.f5_modules.bigiq_utility_license
    bigiq_utility_license_assignment:
      redirect: f5networks.f5_modules.bigiq_utility_license_assignment
    os_auth:
      redirect: openstack.cloud.auth
    os_client_config:
      redirect: openstack.cloud.config
    os_coe_cluster:
      redirect: openstack.cloud.coe_cluster
    os_coe_cluster_template:
      redirect: openstack.cloud.coe_cluster_template
    os_flavor_info:
      redirect: openstack.cloud.compute_flavor_info
    os_floating_ip:
      redirect: openstack.cloud.floating_ip
    os_group:
      redirect: openstack.cloud.identity_group
    os_group_info:
      redirect: openstack.cloud.identity_group_info
    os_image:
      redirect: openstack.cloud.image
    os_image_info:
      redirect: openstack.cloud.image_info
    os_ironic:
      redirect: openstack.cloud.baremetal_node
    os_ironic_inspect:
      redirect: openstack.cloud.baremetal_inspect
    os_ironic_node:
      redirect: openstack.cloud.baremetal_node_action
    os_keypair:
      redirect: openstack.cloud.keypair
    os_keystone_domain:
      redirect: openstack.cloud.identity_domain
    os_keystone_domain_info:
      redirect: openstack.cloud.identity_domain_info
    os_keystone_endpoint:
      redirect: openstack.cloud.endpoint
    os_keystone_role:
      redirect: openstack.cloud.identity_role
    os_keystone_service:
      redirect: openstack.cloud.catalog_service
    os_listener:
      redirect: openstack.cloud.lb_listener
    os_loadbalancer:
      redirect: openstack.cloud.loadbalancer
    os_member:
      redirect: openstack.cloud.lb_member
    os_network:
      redirect: openstack.cloud.network
    os_networks_info:
      redirect: openstack.cloud.networks_info
    os_nova_flavor:
      redirect: openstack.cloud.compute_flavor
    os_nova_host_aggregate:
      redirect: openstack.cloud.host_aggregate
    os_object:
      redirect: openstack.cloud.object
    os_pool:
      redirect: openstack.cloud.lb_pool
    os_port:
      redirect: openstack.cloud.port
    os_port_info:
      redirect: openstack.cloud.port_info
    os_project:
      redirect: openstack.cloud.project
    os_project_access:
      redirect: openstack.cloud.project_access
    os_project_info:
      redirect: openstack.cloud.project_info
    os_quota:
      redirect: openstack.cloud.quota
    os_recordset:
      redirect: openstack.cloud.recordset
    os_router:
      redirect: openstack.cloud.router
    os_security_group:
      redirect: openstack.cloud.security_group
    os_security_group_rule:
      redirect: openstack.cloud.security_group_rule
    os_server:
      redirect: openstack.cloud.server
    os_server_action:
      redirect: openstack.cloud.server_action
    os_server_group:
      redirect: openstack.cloud.server_group
    os_server_info:
      redirect: openstack.cloud.server_info
    os_server_metadata:
      redirect: openstack.cloud.server_metadata
    os_server_volume:
      redirect: openstack.cloud.server_volume
    os_stack:
      redirect: openstack.cloud.stack
    os_subnet:
      redirect: openstack.cloud.subnet
    os_subnets_info:
      redirect: openstack.cloud.subnets_info
    os_user:
      redirect: openstack.cloud.identity_user
    os_user_group:
      redirect: openstack.cloud.group_assignment
    os_user_info:
      redirect: openstack.cloud.identity_user_info
    os_user_role:
      redirect: openstack.cloud.role_assignment
    os_volume:
      redirect: openstack.cloud.volume
    os_volume_snapshot:
      redirect: openstack.cloud.volume_snapshot
    os_zone:
      redirect: openstack.cloud.dns_zone
    junos_acls:
      redirect: junipernetworks.junos.junos_acls
    junos_acl_interfaces:
      redirect: junipernetworks.junos.junos_acl_interfaces
    junos_ospfv2:
      redirect: junipernetworks.junos.junos_ospfv2
    junos_user:
      redirect: junipernetworks.junos.junos_user
    junos_l2_interface:
      redirect: junipernetworks.junos.junos_l2_interface
    junos_lldp:
      redirect: junipernetworks.junos.junos_lldp
    junos_rpc:
      redirect: junipernetworks.junos.junos_rpc
    junos_l2_interfaces:
      redirect: junipernetworks.junos.junos_l2_interfaces
    junos_lldp_interface:
      redirect: junipernetworks.junos.junos_lldp_interface
    junos_static_route:
      redirect: junipernetworks.junos.junos_static_route
    junos_lacp:
      redirect: junipernetworks.junos.junos_lacp
    junos_lacp_interfaces:
      redirect: junipernetworks.junos.junos_lacp_interfaces
    junos_vlans:
      redirect: junipernetworks.junos.junos_vlans
    junos_linkagg:
      redirect: junipernetworks.junos.junos_linkagg
    junos_scp:
      redirect: junipernetworks.junos.junos_scp
    junos_banner:
      redirect: junipernetworks.junos.junos_banner
    junos_l3_interface:
      redirect: junipernetworks.junos.junos_l3_interface
    junos_logging:
      redirect: junipernetworks.junos.junos_logging
    junos_package:
      redirect: junipernetworks.junos.junos_package
    junos_netconf:
      redirect: junipernetworks.junos.junos_netconf
    junos_facts:
      redirect: junipernetworks.junos.junos_facts
    junos_ping:
      redirect: junipernetworks.junos.junos_ping
    junos_interface:
      redirect: junipernetworks.junos.junos_interface
    junos_lldp_global:
      redirect: junipernetworks.junos.junos_lldp_global
    junos_config:
      redirect: junipernetworks.junos.junos_config
    junos_static_routes:
      redirect: junipernetworks.junos.junos_static_routes
    junos_command:
      redirect: junipernetworks.junos.junos_command
    junos_lag_interfaces:
      redirect: junipernetworks.junos.junos_lag_interfaces
    junos_l3_interfaces:
      redirect: junipernetworks.junos.junos_l3_interfaces
    junos_lldp_interfaces:
      redirect: junipernetworks.junos.junos_lldp_interfaces
    junos_vlan:
      redirect: junipernetworks.junos.junos_vlan
    junos_system:
      redirect: junipernetworks.junos.junos_system
    junos_interfaces:
      redirect: junipernetworks.junos.junos_interfaces
    junos_vrf:
      redirect: junipernetworks.junos.junos_vrf
    tower_credential:
      redirect: awx.awx.tower_credential
    tower_credential_type:
      redirect: awx.awx.tower_credential_type
    tower_group:
      redirect: awx.awx.tower_group
    tower_host:
      redirect: awx.awx.tower_host
    tower_inventory:
      redirect: awx.awx.tower_inventory
    tower_inventory_source:
      redirect: awx.awx.tower_inventory_source
    tower_job_cancel:
      redirect: awx.awx.tower_job_cancel
    tower_job_launch:
      redirect: awx.awx.tower_job_launch
    tower_job_list:
      redirect: awx.awx.tower_job_list
    tower_job_template:
      redirect: awx.awx.tower_job_template
    tower_job_wait:
      redirect: awx.awx.tower_job_wait
    tower_label:
      redirect: awx.awx.tower_label
    tower_notification:
      redirect: awx.awx.tower_notification
    tower_organization:
      redirect: awx.awx.tower_organization
    tower_project:
      redirect: awx.awx.tower_project
    tower_receive:
      redirect: awx.awx.tower_receive
    tower_role:
      redirect: awx.awx.tower_role
    tower_send:
      redirect: awx.awx.tower_send
    tower_settings:
      redirect: awx.awx.tower_settings
    tower_team:
      redirect: awx.awx.tower_team
    tower_user:
      redirect: awx.awx.tower_user
    tower_workflow_launch:
      redirect: awx.awx.tower_workflow_launch
    tower_workflow_template:
      redirect: awx.awx.tower_workflow_template
    ovirt_affinity_group:
      redirect: ovirt.ovirt.ovirt_affinity_group
    ovirt_affinity_label:
      redirect: ovirt.ovirt.ovirt_affinity_label
    ovirt_affinity_label_info:
      redirect: ovirt.ovirt.ovirt_affinity_label_info
    ovirt_api_info:
      redirect: ovirt.ovirt.ovirt_api_info
    ovirt_auth:
      redirect: ovirt.ovirt.ovirt_auth
    ovirt_cluster:
      redirect: ovirt.ovirt.ovirt_cluster
    ovirt_cluster_info:
      redirect: ovirt.ovirt.ovirt_cluster_info
    ovirt_datacenter:
      redirect: ovirt.ovirt.ovirt_datacenter
    ovirt_datacenter_info:
      redirect: ovirt.ovirt.ovirt_datacenter_info
    ovirt_disk:
      redirect: ovirt.ovirt.ovirt_disk
    ovirt_disk_info:
      redirect: ovirt.ovirt.ovirt_disk_info
    ovirt_event:
      redirect: ovirt.ovirt.ovirt_event
    ovirt_event_info:
      redirect: ovirt.ovirt.ovirt_event_info
    ovirt_external_provider:
      redirect: ovirt.ovirt.ovirt_external_provider
    ovirt_external_provider_info:
      redirect: ovirt.ovirt.ovirt_external_provider_info
    ovirt_group:
      redirect: ovirt.ovirt.ovirt_group
    ovirt_group_info:
      redirect: ovirt.ovirt.ovirt_group_info
    ovirt_host:
      redirect: ovirt.ovirt.ovirt_host
    ovirt_host_info:
      redirect: ovirt.ovirt.ovirt_host_info
    ovirt_host_network:
      redirect: ovirt.ovirt.ovirt_host_network
    ovirt_host_pm:
      redirect: ovirt.ovirt.ovirt_host_pm
    ovirt_host_storage_info:
      redirect: ovirt.ovirt.ovirt_host_storage_info
    ovirt_instance_type:
      redirect: ovirt.ovirt.ovirt_instance_type
    ovirt_job:
      redirect: ovirt.ovirt.ovirt_job
    ovirt_mac_pool:
      redirect: ovirt.ovirt.ovirt_mac_pool
    ovirt_network:
      redirect: ovirt.ovirt.ovirt_network
    ovirt_network_info:
      redirect: ovirt.ovirt.ovirt_network_info
    ovirt_nic:
      redirect: ovirt.ovirt.ovirt_nic
    ovirt_nic_info:
      redirect: ovirt.ovirt.ovirt_nic_info
    ovirt_permission:
      redirect: ovirt.ovirt.ovirt_permission
    ovirt_permission_info:
      redirect: ovirt.ovirt.ovirt_permission_info
    ovirt_quota:
      redirect: ovirt.ovirt.ovirt_quota
    ovirt_quota_info:
      redirect: ovirt.ovirt.ovirt_quota_info
    ovirt_role:
      redirect: ovirt.ovirt.ovirt_role
    ovirt_scheduling_policy_info:
      redirect: ovirt.ovirt.ovirt_scheduling_policy_info
    ovirt_snapshot:
      redirect: ovirt.ovirt.ovirt_snapshot
    ovirt_snapshot_info:
      redirect: ovirt.ovirt.ovirt_snapshot_info
    ovirt_storage_connection:
      redirect: ovirt.ovirt.ovirt_storage_connection
    ovirt_storage_domain:
      redirect: ovirt.ovirt.ovirt_storage_domain
    ovirt_storage_domain_info:
      redirect: ovirt.ovirt.ovirt_storage_domain_info
    ovirt_storage_template_info:
      redirect: ovirt.ovirt.ovirt_storage_template_info
    ovirt_storage_vm_info:
      redirect: ovirt.ovirt.ovirt_storage_vm_info
    ovirt_tag:
      redirect: ovirt.ovirt.ovirt_tag
    ovirt_tag_info:
      redirect: ovirt.ovirt.ovirt_tag_info
    ovirt_template:
      redirect: ovirt.ovirt.ovirt_template
    ovirt_template_info:
      redirect: ovirt.ovirt.ovirt_template_info
    ovirt_user:
      redirect: ovirt.ovirt.ovirt_user
    ovirt_user_info:
      redirect: ovirt.ovirt.ovirt_user_info
    ovirt_vm:
      redirect: ovirt.ovirt.ovirt_vm
    ovirt_vm_info:
      redirect: ovirt.ovirt.ovirt_vm_info
    ovirt_vmpool:
      redirect: ovirt.ovirt.ovirt_vmpool
    ovirt_vmpool_info:
      redirect: ovirt.ovirt.ovirt_vmpool_info
    ovirt_vnic_profile:
      redirect: ovirt.ovirt.ovirt_vnic_profile
    ovirt_vnic_profile_info:
      redirect: ovirt.ovirt.ovirt_vnic_profile_info
    dellos10_command:
      redirect: dellemc.os10.os10_command
    dellos10_facts:
      redirect: dellemc.os10.os10_facts
    dellos10_config:
      redirect: dellemc.os10.os10_config
    dellos9_facts:
      redirect: dellemc.os9.os9_facts
    dellos9_command:
      redirect: dellemc.os9.os9_command
    dellos9_config:
      redirect: dellemc.os9.os9_config
    dellos6_facts:
      redirect: dellemc.os6.os6_facts
    dellos6_config:
      redirect: dellemc.os6.os6_config
    dellos6_command:
      redirect: dellemc.os6.os6_command
    hcloud_location_facts:
      redirect: hetzner.hcloud.hcloud_location_facts
    hcloud_server_info:
      redirect: hetzner.hcloud.hcloud_server_info
    hcloud_server_network:
      redirect: hetzner.hcloud.hcloud_server_network
    hcloud_server_type_info:
      redirect: hetzner.hcloud.hcloud_server_type_info
    hcloud_route:
      redirect: hetzner.hcloud.hcloud_route
    hcloud_server:
      redirect: hetzner.hcloud.hcloud_server
    hcloud_volume_info:
      redirect: hetzner.hcloud.hcloud_volume_info
    hcloud_server_type_facts:
      redirect: hetzner.hcloud.hcloud_server_type_facts
    hcloud_ssh_key_info:
      redirect: hetzner.hcloud.hcloud_ssh_key_info
    hcloud_network_info:
      redirect: hetzner.hcloud.hcloud_network_info
    hcloud_datacenter_info:
      redirect: hetzner.hcloud.hcloud_datacenter_info
    hcloud_image_facts:
      redirect: hetzner.hcloud.hcloud_image_facts
    hcloud_volume_facts:
      redirect: hetzner.hcloud.hcloud_volume_facts
    hcloud_floating_ip_info:
      redirect: hetzner.hcloud.hcloud_floating_ip_info
    hcloud_floating_ip_facts:
      redirect: hetzner.hcloud.hcloud_floating_ip_facts
    hcloud_image_info:
      redirect: hetzner.hcloud.hcloud_image_info
    hcloud_ssh_key_facts:
      redirect: hetzner.hcloud.hcloud_ssh_key_facts
    hcloud_location_info:
      redirect: hetzner.hcloud.hcloud_location_info
    hcloud_network:
      redirect: hetzner.hcloud.hcloud_network
    hcloud_volume:
      redirect: hetzner.hcloud.hcloud_volume
    hcloud_ssh_key:
      redirect: hetzner.hcloud.hcloud_ssh_key
    hcloud_datacenter_facts:
      redirect: hetzner.hcloud.hcloud_datacenter_facts
    hcloud_rdns:
      redirect: hetzner.hcloud.hcloud_rdns
    hcloud_floating_ip:
      redirect: hetzner.hcloud.hcloud_floating_ip
    hcloud_server_facts:
      redirect: hetzner.hcloud.hcloud_server_facts
    hcloud_subnetwork:
      redirect: hetzner.hcloud.hcloud_subnetwork
    skydive_capture:
      redirect: community.skydive.skydive_capture
    skydive_edge:
      redirect: community.skydive.skydive_edge
    skydive_node:
      redirect: community.skydive.skydive_node
    cyberark_authentication:
      redirect: cyberark.pas.cyberark_authentication
    cyberark_user:
      redirect: cyberark.pas.cyberark_user
    gcp_appengine_firewall_rule:
      redirect: google.cloud.gcp_appengine_firewall_rule
    gcp_appengine_firewall_rule_info:
      redirect: google.cloud.gcp_appengine_firewall_rule_info
    gcp_bigquery_dataset:
      redirect: google.cloud.gcp_bigquery_dataset
    gcp_bigquery_dataset_info:
      redirect: google.cloud.gcp_bigquery_dataset_info
    gcp_bigquery_table:
      redirect: google.cloud.gcp_bigquery_table
    gcp_bigquery_table_info:
      redirect: google.cloud.gcp_bigquery_table_info
    gcp_cloudbuild_trigger:
      redirect: google.cloud.gcp_cloudbuild_trigger
    gcp_cloudbuild_trigger_info:
      redirect: google.cloud.gcp_cloudbuild_trigger_info
    gcp_cloudfunctions_cloud_function:
      redirect: google.cloud.gcp_cloudfunctions_cloud_function
    gcp_cloudfunctions_cloud_function_info:
      redirect: google.cloud.gcp_cloudfunctions_cloud_function_info
    gcp_cloudscheduler_job:
      redirect: google.cloud.gcp_cloudscheduler_job
    gcp_cloudscheduler_job_info:
      redirect: google.cloud.gcp_cloudscheduler_job_info
    gcp_cloudtasks_queue:
      redirect: google.cloud.gcp_cloudtasks_queue
    gcp_cloudtasks_queue_info:
      redirect: google.cloud.gcp_cloudtasks_queue_info
    gcp_compute_address:
      redirect: google.cloud.gcp_compute_address
    gcp_compute_address_info:
      redirect: google.cloud.gcp_compute_address_info
    gcp_compute_autoscaler:
      redirect: google.cloud.gcp_compute_autoscaler
    gcp_compute_autoscaler_info:
      redirect: google.cloud.gcp_compute_autoscaler_info
    gcp_compute_backend_bucket:
      redirect: google.cloud.gcp_compute_backend_bucket
    gcp_compute_backend_bucket_info:
      redirect: google.cloud.gcp_compute_backend_bucket_info
    gcp_compute_backend_service:
      redirect: google.cloud.gcp_compute_backend_service
    gcp_compute_backend_service_info:
      redirect: google.cloud.gcp_compute_backend_service_info
    gcp_compute_disk:
      redirect: google.cloud.gcp_compute_disk
    gcp_compute_disk_info:
      redirect: google.cloud.gcp_compute_disk_info
    gcp_compute_firewall:
      redirect: google.cloud.gcp_compute_firewall
    gcp_compute_firewall_info:
      redirect: google.cloud.gcp_compute_firewall_info
    gcp_compute_forwarding_rule:
      redirect: google.cloud.gcp_compute_forwarding_rule
    gcp_compute_forwarding_rule_info:
      redirect: google.cloud.gcp_compute_forwarding_rule_info
    gcp_compute_global_address:
      redirect: google.cloud.gcp_compute_global_address
    gcp_compute_global_address_info:
      redirect: google.cloud.gcp_compute_global_address_info
    gcp_compute_global_forwarding_rule:
      redirect: google.cloud.gcp_compute_global_forwarding_rule
    gcp_compute_global_forwarding_rule_info:
      redirect: google.cloud.gcp_compute_global_forwarding_rule_info
    gcp_compute_health_check:
      redirect: google.cloud.gcp_compute_health_check
    gcp_compute_health_check_info:
      redirect: google.cloud.gcp_compute_health_check_info
    gcp_compute_http_health_check:
      redirect: google.cloud.gcp_compute_http_health_check
    gcp_compute_http_health_check_info:
      redirect: google.cloud.gcp_compute_http_health_check_info
    gcp_compute_https_health_check:
      redirect: google.cloud.gcp_compute_https_health_check
    gcp_compute_https_health_check_info:
      redirect: google.cloud.gcp_compute_https_health_check_info
    gcp_compute_image:
      redirect: google.cloud.gcp_compute_image
    gcp_compute_image_info:
      redirect: google.cloud.gcp_compute_image_info
    gcp_compute_instance:
      redirect: google.cloud.gcp_compute_instance
    gcp_compute_instance_group:
      redirect: google.cloud.gcp_compute_instance_group
    gcp_compute_instance_group_info:
      redirect: google.cloud.gcp_compute_instance_group_info
    gcp_compute_instance_group_manager:
      redirect: google.cloud.gcp_compute_instance_group_manager
    gcp_compute_instance_group_manager_info:
      redirect: google.cloud.gcp_compute_instance_group_manager_info
    gcp_compute_instance_info:
      redirect: google.cloud.gcp_compute_instance_info
    gcp_compute_instance_template:
      redirect: google.cloud.gcp_compute_instance_template
    gcp_compute_instance_template_info:
      redirect: google.cloud.gcp_compute_instance_template_info
    gcp_compute_interconnect_attachment:
      redirect: google.cloud.gcp_compute_interconnect_attachment
    gcp_compute_interconnect_attachment_info:
      redirect: google.cloud.gcp_compute_interconnect_attachment_info
    gcp_compute_network:
      redirect: google.cloud.gcp_compute_network
    gcp_compute_network_endpoint_group:
      redirect: google.cloud.gcp_compute_network_endpoint_group
    gcp_compute_network_endpoint_group_info:
      redirect: google.cloud.gcp_compute_network_endpoint_group_info
    gcp_compute_network_info:
      redirect: google.cloud.gcp_compute_network_info
    gcp_compute_node_group:
      redirect: google.cloud.gcp_compute_node_group
    gcp_compute_node_group_info:
      redirect: google.cloud.gcp_compute_node_group_info
    gcp_compute_node_template:
      redirect: google.cloud.gcp_compute_node_template
    gcp_compute_node_template_info:
      redirect: google.cloud.gcp_compute_node_template_info
    gcp_compute_region_backend_service:
      redirect: google.cloud.gcp_compute_region_backend_service
    gcp_compute_region_backend_service_info:
      redirect: google.cloud.gcp_compute_region_backend_service_info
    gcp_compute_region_disk:
      redirect: google.cloud.gcp_compute_region_disk
    gcp_compute_region_disk_info:
      redirect: google.cloud.gcp_compute_region_disk_info
    gcp_compute_reservation:
      redirect: google.cloud.gcp_compute_reservation
    gcp_compute_reservation_info:
      redirect: google.cloud.gcp_compute_reservation_info
    gcp_compute_route:
      redirect: google.cloud.gcp_compute_route
    gcp_compute_route_info:
      redirect: google.cloud.gcp_compute_route_info
    gcp_compute_router:
      redirect: google.cloud.gcp_compute_router
    gcp_compute_router_info:
      redirect: google.cloud.gcp_compute_router_info
    gcp_compute_snapshot:
      redirect: google.cloud.gcp_compute_snapshot
    gcp_compute_snapshot_info:
      redirect: google.cloud.gcp_compute_snapshot_info
    gcp_compute_ssl_certificate:
      redirect: google.cloud.gcp_compute_ssl_certificate
    gcp_compute_ssl_certificate_info:
      redirect: google.cloud.gcp_compute_ssl_certificate_info
    gcp_compute_ssl_policy:
      redirect: google.cloud.gcp_compute_ssl_policy
    gcp_compute_ssl_policy_info:
      redirect: google.cloud.gcp_compute_ssl_policy_info
    gcp_compute_subnetwork:
      redirect: google.cloud.gcp_compute_subnetwork
    gcp_compute_subnetwork_info:
      redirect: google.cloud.gcp_compute_subnetwork_info
    gcp_compute_target_http_proxy:
      redirect: google.cloud.gcp_compute_target_http_proxy
    gcp_compute_target_http_proxy_info:
      redirect: google.cloud.gcp_compute_target_http_proxy_info
    gcp_compute_target_https_proxy:
      redirect: google.cloud.gcp_compute_target_https_proxy
    gcp_compute_target_https_proxy_info:
      redirect: google.cloud.gcp_compute_target_https_proxy_info
    gcp_compute_target_instance:
      redirect: google.cloud.gcp_compute_target_instance
    gcp_compute_target_instance_info:
      redirect: google.cloud.gcp_compute_target_instance_info
    gcp_compute_target_pool:
      redirect: google.cloud.gcp_compute_target_pool
    gcp_compute_target_pool_info:
      redirect: google.cloud.gcp_compute_target_pool_info
    gcp_compute_target_ssl_proxy:
      redirect: google.cloud.gcp_compute_target_ssl_proxy
    gcp_compute_target_ssl_proxy_info:
      redirect: google.cloud.gcp_compute_target_ssl_proxy_info
    gcp_compute_target_tcp_proxy:
      redirect: google.cloud.gcp_compute_target_tcp_proxy
    gcp_compute_target_tcp_proxy_info:
      redirect: google.cloud.gcp_compute_target_tcp_proxy_info
    gcp_compute_target_vpn_gateway:
      redirect: google.cloud.gcp_compute_target_vpn_gateway
    gcp_compute_target_vpn_gateway_info:
      redirect: google.cloud.gcp_compute_target_vpn_gateway_info
    gcp_compute_url_map:
      redirect: google.cloud.gcp_compute_url_map
    gcp_compute_url_map_info:
      redirect: google.cloud.gcp_compute_url_map_info
    gcp_compute_vpn_tunnel:
      redirect: google.cloud.gcp_compute_vpn_tunnel
    gcp_compute_vpn_tunnel_info:
      redirect: google.cloud.gcp_compute_vpn_tunnel_info
    gcp_container_cluster:
      redirect: google.cloud.gcp_container_cluster
    gcp_container_cluster_info:
      redirect: google.cloud.gcp_container_cluster_info
    gcp_container_node_pool:
      redirect: google.cloud.gcp_container_node_pool
    gcp_container_node_pool_info:
      redirect: google.cloud.gcp_container_node_pool_info
    gcp_dns_managed_zone:
      redirect: google.cloud.gcp_dns_managed_zone
    gcp_dns_managed_zone_info:
      redirect: google.cloud.gcp_dns_managed_zone_info
    gcp_dns_resource_record_set:
      redirect: google.cloud.gcp_dns_resource_record_set
    gcp_dns_resource_record_set_info:
      redirect: google.cloud.gcp_dns_resource_record_set_info
    gcp_filestore_instance:
      redirect: google.cloud.gcp_filestore_instance
    gcp_filestore_instance_info:
      redirect: google.cloud.gcp_filestore_instance_info
    gcp_iam_role:
      redirect: google.cloud.gcp_iam_role
    gcp_iam_role_info:
      redirect: google.cloud.gcp_iam_role_info
    gcp_iam_service_account:
      redirect: google.cloud.gcp_iam_service_account
    gcp_iam_service_account_info:
      redirect: google.cloud.gcp_iam_service_account_info
    gcp_iam_service_account_key:
      redirect: google.cloud.gcp_iam_service_account_key
    gcp_kms_crypto_key:
      redirect: google.cloud.gcp_kms_crypto_key
    gcp_kms_crypto_key_info:
      redirect: google.cloud.gcp_kms_crypto_key_info
    gcp_kms_key_ring:
      redirect: google.cloud.gcp_kms_key_ring
    gcp_kms_key_ring_info:
      redirect: google.cloud.gcp_kms_key_ring_info
    gcp_logging_metric:
      redirect: google.cloud.gcp_logging_metric
    gcp_logging_metric_info:
      redirect: google.cloud.gcp_logging_metric_info
    gcp_mlengine_model:
      redirect: google.cloud.gcp_mlengine_model
    gcp_mlengine_model_info:
      redirect: google.cloud.gcp_mlengine_model_info
    gcp_mlengine_version:
      redirect: google.cloud.gcp_mlengine_version
    gcp_mlengine_version_info:
      redirect: google.cloud.gcp_mlengine_version_info
    gcp_pubsub_subscription:
      redirect: google.cloud.gcp_pubsub_subscription
    gcp_pubsub_subscription_info:
      redirect: google.cloud.gcp_pubsub_subscription_info
    gcp_pubsub_topic:
      redirect: google.cloud.gcp_pubsub_topic
    gcp_pubsub_topic_info:
      redirect: google.cloud.gcp_pubsub_topic_info
    gcp_redis_instance:
      redirect: google.cloud.gcp_redis_instance
    gcp_redis_instance_info:
      redirect: google.cloud.gcp_redis_instance_info
    gcp_resourcemanager_project:
      redirect: google.cloud.gcp_resourcemanager_project
    gcp_resourcemanager_project_info:
      redirect: google.cloud.gcp_resourcemanager_project_info
    gcp_runtimeconfig_config:
      redirect: google.cloud.gcp_runtimeconfig_config
    gcp_runtimeconfig_config_info:
      redirect: google.cloud.gcp_runtimeconfig_config_info
    gcp_runtimeconfig_variable:
      redirect: google.cloud.gcp_runtimeconfig_variable
    gcp_runtimeconfig_variable_info:
      redirect: google.cloud.gcp_runtimeconfig_variable_info
    gcp_serviceusage_service:
      redirect: google.cloud.gcp_serviceusage_service
    gcp_serviceusage_service_info:
      redirect: google.cloud.gcp_serviceusage_service_info
    gcp_sourcerepo_repository:
      redirect: google.cloud.gcp_sourcerepo_repository
    gcp_sourcerepo_repository_info:
      redirect: google.cloud.gcp_sourcerepo_repository_info
    gcp_spanner_database:
      redirect: google.cloud.gcp_spanner_database
    gcp_spanner_database_info:
      redirect: google.cloud.gcp_spanner_database_info
    gcp_spanner_instance:
      redirect: google.cloud.gcp_spanner_instance
    gcp_spanner_instance_info:
      redirect: google.cloud.gcp_spanner_instance_info
    gcp_sql_database:
      redirect: google.cloud.gcp_sql_database
    gcp_sql_database_info:
      redirect: google.cloud.gcp_sql_database_info
    gcp_sql_instance:
      redirect: google.cloud.gcp_sql_instance
    gcp_sql_instance_info:
      redirect: google.cloud.gcp_sql_instance_info
    gcp_sql_user:
      redirect: google.cloud.gcp_sql_user
    gcp_sql_user_info:
      redirect: google.cloud.gcp_sql_user_info
    gcp_storage_bucket:
      redirect: google.cloud.gcp_storage_bucket
    gcp_storage_bucket_access_control:
      redirect: google.cloud.gcp_storage_bucket_access_control
    gcp_storage_object:
      redirect: google.cloud.gcp_storage_object
    gcp_tpu_node:
      redirect: google.cloud.gcp_tpu_node
    gcp_tpu_node_info:
      redirect: google.cloud.gcp_tpu_node_info
    purefa_alert:
      redirect: purestorage.flasharray.purefa_alert
    purefa_arrayname:
      redirect: purestorage.flasharray.purefa_arrayname
    purefa_banner:
      redirect: purestorage.flasharray.purefa_banner
    purefa_connect:
      redirect: purestorage.flasharray.purefa_connect
    purefa_dns:
      redirect: purestorage.flasharray.purefa_dns
    purefa_ds:
      redirect: purestorage.flasharray.purefa_ds
    purefa_dsrole:
      redirect: purestorage.flasharray.purefa_dsrole
    purefa_hg:
      redirect: purestorage.flasharray.purefa_hg
    purefa_host:
      redirect: purestorage.flasharray.purefa_host
    purefa_info:
      redirect: purestorage.flasharray.purefa_info
    purefa_ntp:
      redirect: purestorage.flasharray.purefa_ntp
    purefa_offload:
      redirect: purestorage.flasharray.purefa_offload
    purefa_pg:
      redirect: purestorage.flasharray.purefa_pg
    purefa_pgsnap:
      redirect: purestorage.flasharray.purefa_pgsnap
    purefa_phonehome:
      redirect: purestorage.flasharray.purefa_phonehome
    purefa_ra:
      redirect: purestorage.flasharray.purefa_ra
    purefa_smtp:
      redirect: purestorage.flasharray.purefa_smtp
    purefa_snap:
      redirect: purestorage.flasharray.purefa_snap
    purefa_snmp:
      redirect: purestorage.flasharray.purefa_snmp
    purefa_syslog:
      redirect: purestorage.flasharray.purefa_syslog
    purefa_user:
      redirect: purestorage.flasharray.purefa_user
    purefa_vg:
      redirect: purestorage.flasharray.purefa_vg
    purefa_volume:
      redirect: purestorage.flasharray.purefa_volume
    purefb_bucket:
      redirect: purestorage.flashblade.purefb_bucket
    purefb_ds:
      redirect: purestorage.flashblade.purefb_ds
    purefb_dsrole:
      redirect: purestorage.flashblade.purefb_dsrole
    purefb_fs:
      redirect: purestorage.flashblade.purefb_fs
    purefb_info:
      redirect: purestorage.flashblade.purefb_info
    purefb_network:
      redirect: purestorage.flashblade.purefb_network
    purefb_ra:
      redirect: purestorage.flashblade.purefb_ra
    purefb_s3acc:
      redirect: purestorage.flashblade.purefb_s3acc
    purefb_s3user:
      redirect: purestorage.flashblade.purefb_s3user
    purefb_smtp:
      redirect: purestorage.flashblade.purefb_smtp
    purefb_snap:
      redirect: purestorage.flashblade.purefb_snap
    purefb_subnet:
      redirect: purestorage.flashblade.purefb_subnet
    azure_rm_acs:
      redirect: azure.azcollection.azure_rm_acs
    azure_rm_virtualmachine_info:
      redirect: azure.azcollection.azure_rm_virtualmachine_info
    azure_rm_dnsrecordset_info:
      redirect: azure.azcollection.azure_rm_dnsrecordset_info
    azure_rm_dnszone_info:
      redirect: azure.azcollection.azure_rm_dnszone_info
    azure_rm_networkinterface_info:
      redirect: azure.azcollection.azure_rm_networkinterface_info
    azure_rm_publicipaddress_info:
      redirect: azure.azcollection.azure_rm_publicipaddress_info
    azure_rm_securitygroup_info:
      redirect: azure.azcollection.azure_rm_securitygroup_info
    azure_rm_storageaccount_info:
      redirect: azure.azcollection.azure_rm_storageaccount_info
    azure_rm_virtualnetwork_info:
      redirect: azure.azcollection.azure_rm_virtualnetwork_info
    azure_rm_deployment:
      redirect: azure.azcollection.azure_rm_deployment
    azure_rm_dnsrecordset:
      redirect: azure.azcollection.azure_rm_dnsrecordset
    azure_rm_dnszone:
      redirect: azure.azcollection.azure_rm_dnszone
    azure_rm_networkinterface:
      redirect: azure.azcollection.azure_rm_networkinterface
    azure_rm_publicipaddress:
      redirect: azure.azcollection.azure_rm_publicipaddress
    azure_rm_securitygroup:
      redirect: azure.azcollection.azure_rm_securitygroup
    azure_rm_storageaccount:
      redirect: azure.azcollection.azure_rm_storageaccount
    azure_rm_subnet:
      redirect: azure.azcollection.azure_rm_subnet
    azure_rm_virtualmachine:
      redirect: azure.azcollection.azure_rm_virtualmachine
    azure_rm_virtualnetwork:
      redirect: azure.azcollection.azure_rm_virtualnetwork
    azure_rm_aks:
      redirect: azure.azcollection.azure_rm_aks
    azure_rm_aks_info:
      redirect: azure.azcollection.azure_rm_aks_info
    azure_rm_aksversion_info:
      redirect: azure.azcollection.azure_rm_aksversion_info
    azure_rm_appgateway:
      redirect: azure.azcollection.azure_rm_appgateway
    azure_rm_applicationsecuritygroup:
      redirect: azure.azcollection.azure_rm_applicationsecuritygroup
    azure_rm_applicationsecuritygroup_info:
      redirect: azure.azcollection.azure_rm_applicationsecuritygroup_info
    azure_rm_appserviceplan:
      redirect: azure.azcollection.azure_rm_appserviceplan
    azure_rm_appserviceplan_info:
      redirect: azure.azcollection.azure_rm_appserviceplan_info
    azure_rm_availabilityset:
      redirect: azure.azcollection.azure_rm_availabilityset
    azure_rm_availabilityset_info:
      redirect: azure.azcollection.azure_rm_availabilityset_info
    azure_rm_containerinstance:
      redirect: azure.azcollection.azure_rm_containerinstance
    azure_rm_containerinstance_info:
      redirect: azure.azcollection.azure_rm_containerinstance_info
    azure_rm_containerregistry:
      redirect: azure.azcollection.azure_rm_containerregistry
    azure_rm_containerregistry_info:
      redirect: azure.azcollection.azure_rm_containerregistry_info
    azure_rm_deployment_info:
      redirect: azure.azcollection.azure_rm_deployment_info
    azure_rm_functionapp:
      redirect: azure.azcollection.azure_rm_functionapp
    azure_rm_functionapp_info:
      redirect: azure.azcollection.azure_rm_functionapp_info
    azure_rm_gallery:
      redirect: azure.azcollection.azure_rm_gallery
    azure_rm_gallery_info:
      redirect: azure.azcollection.azure_rm_gallery_info
    azure_rm_galleryimage:
      redirect: azure.azcollection.azure_rm_galleryimage
    azure_rm_galleryimage_info:
      redirect: azure.azcollection.azure_rm_galleryimage_info
    azure_rm_galleryimageversion:
      redirect: azure.azcollection.azure_rm_galleryimageversion
    azure_rm_galleryimageversion_info:
      redirect: azure.azcollection.azure_rm_galleryimageversion_info
    azure_rm_image:
      redirect: azure.azcollection.azure_rm_image
    azure_rm_image_info:
      redirect: azure.azcollection.azure_rm_image_info
    azure_rm_keyvault:
      redirect: azure.azcollection.azure_rm_keyvault
    azure_rm_keyvault_info:
      redirect: azure.azcollection.azure_rm_keyvault_info
    azure_rm_keyvaultkey:
      redirect: azure.azcollection.azure_rm_keyvaultkey
    azure_rm_keyvaultkey_info:
      redirect: azure.azcollection.azure_rm_keyvaultkey_info
    azure_rm_keyvaultsecret:
      redirect: azure.azcollection.azure_rm_keyvaultsecret
    azure_rm_manageddisk:
      redirect: azure.azcollection.azure_rm_manageddisk
    azure_rm_manageddisk_info:
      redirect: azure.azcollection.azure_rm_manageddisk_info
    azure_rm_resource:
      redirect: azure.azcollection.azure_rm_resource
    azure_rm_resource_info:
      redirect: azure.azcollection.azure_rm_resource_info
    azure_rm_resourcegroup:
      redirect: azure.azcollection.azure_rm_resourcegroup
    azure_rm_resourcegroup_info:
      redirect: azure.azcollection.azure_rm_resourcegroup_info
    azure_rm_snapshot:
      redirect: azure.azcollection.azure_rm_snapshot
    azure_rm_storageblob:
      redirect: azure.azcollection.azure_rm_storageblob
    azure_rm_subnet_info:
      redirect: azure.azcollection.azure_rm_subnet_info
    azure_rm_virtualmachineextension:
      redirect: azure.azcollection.azure_rm_virtualmachineextension
    azure_rm_virtualmachineextension_info:
      redirect: azure.azcollection.azure_rm_virtualmachineextension_info
    azure_rm_virtualmachineimage_info:
      redirect: azure.azcollection.azure_rm_virtualmachineimage_info
    azure_rm_virtualmachinescaleset:
      redirect: azure.azcollection.azure_rm_virtualmachinescaleset
    azure_rm_virtualmachinescaleset_info:
      redirect: azure.azcollection.azure_rm_virtualmachinescaleset_info
    azure_rm_virtualmachinescalesetextension:
      redirect: azure.azcollection.azure_rm_virtualmachinescalesetextension
    azure_rm_virtualmachinescalesetextension_info:
      redirect: azure.azcollection.azure_rm_virtualmachinescalesetextension_info
    azure_rm_virtualmachinescalesetinstance:
      redirect: azure.azcollection.azure_rm_virtualmachinescalesetinstance
    azure_rm_virtualmachinescalesetinstance_info:
      redirect: azure.azcollection.azure_rm_virtualmachinescalesetinstance_info
    azure_rm_webapp:
      redirect: azure.azcollection.azure_rm_webapp
    azure_rm_webapp_info:
      redirect: azure.azcollection.azure_rm_webapp_info
    azure_rm_webappslot:
      redirect: azure.azcollection.azure_rm_webappslot
    azure_rm_automationaccount:
      redirect: azure.azcollection.azure_rm_automationaccount
    azure_rm_automationaccount_info:
      redirect: azure.azcollection.azure_rm_automationaccount_info
    azure_rm_autoscale:
      redirect: azure.azcollection.azure_rm_autoscale
    azure_rm_autoscale_info:
      redirect: azure.azcollection.azure_rm_autoscale_info
    azure_rm_azurefirewall:
      redirect: azure.azcollection.azure_rm_azurefirewall
    azure_rm_azurefirewall_info:
      redirect: azure.azcollection.azure_rm_azurefirewall_info
    azure_rm_batchaccount:
      redirect: azure.azcollection.azure_rm_batchaccount
    azure_rm_cdnendpoint:
      redirect: azure.azcollection.azure_rm_cdnendpoint
    azure_rm_cdnendpoint_info:
      redirect: azure.azcollection.azure_rm_cdnendpoint_info
    azure_rm_cdnprofile:
      redirect: azure.azcollection.azure_rm_cdnprofile
    azure_rm_cdnprofile_info:
      redirect: azure.azcollection.azure_rm_cdnprofile_info
    azure_rm_iotdevice:
      redirect: azure.azcollection.azure_rm_iotdevice
    azure_rm_iotdevice_info:
      redirect: azure.azcollection.azure_rm_iotdevice_info
    azure_rm_iotdevicemodule:
      redirect: azure.azcollection.azure_rm_iotdevicemodule
    azure_rm_iothub:
      redirect: azure.azcollection.azure_rm_iothub
    azure_rm_iothub_info:
      redirect: azure.azcollection.azure_rm_iothub_info
    azure_rm_iothubconsumergroup:
      redirect: azure.azcollection.azure_rm_iothubconsumergroup
    azure_rm_loadbalancer:
      redirect: azure.azcollection.azure_rm_loadbalancer
    azure_rm_loadbalancer_info:
      redirect: azure.azcollection.azure_rm_loadbalancer_info
    azure_rm_lock:
      redirect: azure.azcollection.azure_rm_lock
    azure_rm_lock_info:
      redirect: azure.azcollection.azure_rm_lock_info
    azure_rm_loganalyticsworkspace:
      redirect: azure.azcollection.azure_rm_loganalyticsworkspace
    azure_rm_loganalyticsworkspace_info:
      redirect: azure.azcollection.azure_rm_loganalyticsworkspace_info
    azure_rm_monitorlogprofile:
      redirect: azure.azcollection.azure_rm_monitorlogprofile
    azure_rm_rediscache:
      redirect: azure.azcollection.azure_rm_rediscache
    azure_rm_rediscache_info:
      redirect: azure.azcollection.azure_rm_rediscache_info
    azure_rm_rediscachefirewallrule:
      redirect: azure.azcollection.azure_rm_rediscachefirewallrule
    azure_rm_roleassignment:
      redirect: azure.azcollection.azure_rm_roleassignment
    azure_rm_roleassignment_info:
      redirect: azure.azcollection.azure_rm_roleassignment_info
    azure_rm_roledefinition:
      redirect: azure.azcollection.azure_rm_roledefinition
    azure_rm_roledefinition_info:
      redirect: azure.azcollection.azure_rm_roledefinition_info
    azure_rm_route:
      redirect: azure.azcollection.azure_rm_route
    azure_rm_routetable:
      redirect: azure.azcollection.azure_rm_routetable
    azure_rm_routetable_info:
      redirect: azure.azcollection.azure_rm_routetable_info
    azure_rm_servicebus:
      redirect: azure.azcollection.azure_rm_servicebus
    azure_rm_servicebus_info:
      redirect: azure.azcollection.azure_rm_servicebus_info
    azure_rm_servicebusqueue:
      redirect: azure.azcollection.azure_rm_servicebusqueue
    azure_rm_servicebussaspolicy:
      redirect: azure.azcollection.azure_rm_servicebussaspolicy
    azure_rm_servicebustopic:
      redirect: azure.azcollection.azure_rm_servicebustopic
    azure_rm_servicebustopicsubscription:
      redirect: azure.azcollection.azure_rm_servicebustopicsubscription
    azure_rm_trafficmanagerendpoint:
      redirect: azure.azcollection.azure_rm_trafficmanagerendpoint
    azure_rm_trafficmanagerendpoint_info:
      redirect: azure.azcollection.azure_rm_trafficmanagerendpoint_info
    azure_rm_trafficmanagerprofile:
      redirect: azure.azcollection.azure_rm_trafficmanagerprofile
    azure_rm_trafficmanagerprofile_info:
      redirect: azure.azcollection.azure_rm_trafficmanagerprofile_info
    azure_rm_virtualnetworkgateway:
      redirect: azure.azcollection.azure_rm_virtualnetworkgateway
    azure_rm_virtualnetworkpeering:
      redirect: azure.azcollection.azure_rm_virtualnetworkpeering
    azure_rm_virtualnetworkpeering_info:
      redirect: azure.azcollection.azure_rm_virtualnetworkpeering_info
    azure_rm_cosmosdbaccount:
      redirect: azure.azcollection.azure_rm_cosmosdbaccount
    azure_rm_cosmosdbaccount_info:
      redirect: azure.azcollection.azure_rm_cosmosdbaccount_info
    azure_rm_devtestlab:
      redirect: azure.azcollection.azure_rm_devtestlab
    azure_rm_devtestlab_info:
      redirect: azure.azcollection.azure_rm_devtestlab_info
    azure_rm_devtestlabarmtemplate_info:
      redirect: azure.azcollection.azure_rm_devtestlabarmtemplate_info
    azure_rm_devtestlabartifact_info:
      redirect: azure.azcollection.azure_rm_devtestlabartifact_info
    azure_rm_devtestlabartifactsource:
      redirect: azure.azcollection.azure_rm_devtestlabartifactsource
    azure_rm_devtestlabartifactsource_info:
      redirect: azure.azcollection.azure_rm_devtestlabartifactsource_info
    azure_rm_devtestlabcustomimage:
      redirect: azure.azcollection.azure_rm_devtestlabcustomimage
    azure_rm_devtestlabcustomimage_info:
      redirect: azure.azcollection.azure_rm_devtestlabcustomimage_info
    azure_rm_devtestlabenvironment:
      redirect: azure.azcollection.azure_rm_devtestlabenvironment
    azure_rm_devtestlabenvironment_info:
      redirect: azure.azcollection.azure_rm_devtestlabenvironment_info
    azure_rm_devtestlabpolicy:
      redirect: azure.azcollection.azure_rm_devtestlabpolicy
    azure_rm_devtestlabpolicy_info:
      redirect: azure.azcollection.azure_rm_devtestlabpolicy_info
    azure_rm_devtestlabschedule:
      redirect: azure.azcollection.azure_rm_devtestlabschedule
    azure_rm_devtestlabschedule_info:
      redirect: azure.azcollection.azure_rm_devtestlabschedule_info
    azure_rm_devtestlabvirtualmachine:
      redirect: azure.azcollection.azure_rm_devtestlabvirtualmachine
    azure_rm_devtestlabvirtualmachine_info:
      redirect: azure.azcollection.azure_rm_devtestlabvirtualmachine_info
    azure_rm_devtestlabvirtualnetwork:
      redirect: azure.azcollection.azure_rm_devtestlabvirtualnetwork
    azure_rm_devtestlabvirtualnetwork_info:
      redirect: azure.azcollection.azure_rm_devtestlabvirtualnetwork_info
    azure_rm_hdinsightcluster:
      redirect: azure.azcollection.azure_rm_hdinsightcluster
    azure_rm_hdinsightcluster_info:
      redirect: azure.azcollection.azure_rm_hdinsightcluster_info
    azure_rm_mariadbconfiguration:
      redirect: azure.azcollection.azure_rm_mariadbconfiguration
    azure_rm_mariadbconfiguration_info:
      redirect: azure.azcollection.azure_rm_mariadbconfiguration_info
    azure_rm_mariadbdatabase:
      redirect: azure.azcollection.azure_rm_mariadbdatabase
    azure_rm_mariadbdatabase_info:
      redirect: azure.azcollection.azure_rm_mariadbdatabase_info
    azure_rm_mariadbfirewallrule:
      redirect: azure.azcollection.azure_rm_mariadbfirewallrule
    azure_rm_mariadbfirewallrule_info:
      redirect: azure.azcollection.azure_rm_mariadbfirewallrule_info
    azure_rm_mariadbserver:
      redirect: azure.azcollection.azure_rm_mariadbserver
    azure_rm_mariadbserver_info:
      redirect: azure.azcollection.azure_rm_mariadbserver_info
    azure_rm_mysqlconfiguration:
      redirect: azure.azcollection.azure_rm_mysqlconfiguration
    azure_rm_mysqlconfiguration_info:
      redirect: azure.azcollection.azure_rm_mysqlconfiguration_info
    azure_rm_mysqldatabase:
      redirect: azure.azcollection.azure_rm_mysqldatabase
    azure_rm_mysqldatabase_info:
      redirect: azure.azcollection.azure_rm_mysqldatabase_info
    azure_rm_mysqlfirewallrule:
      redirect: azure.azcollection.azure_rm_mysqlfirewallrule
    azure_rm_mysqlfirewallrule_info:
      redirect: azure.azcollection.azure_rm_mysqlfirewallrule_info
    azure_rm_mysqlserver:
      redirect: azure.azcollection.azure_rm_mysqlserver
    azure_rm_mysqlserver_info:
      redirect: azure.azcollection.azure_rm_mysqlserver_info
    azure_rm_postgresqlconfiguration:
      redirect: azure.azcollection.azure_rm_postgresqlconfiguration
    azure_rm_postgresqlconfiguration_info:
      redirect: azure.azcollection.azure_rm_postgresqlconfiguration_info
    azure_rm_postgresqldatabase:
      redirect: azure.azcollection.azure_rm_postgresqldatabase
    azure_rm_postgresqldatabase_info:
      redirect: azure.azcollection.azure_rm_postgresqldatabase_info
    azure_rm_postgresqlfirewallrule:
      redirect: azure.azcollection.azure_rm_postgresqlfirewallrule
    azure_rm_postgresqlfirewallrule_info:
      redirect: azure.azcollection.azure_rm_postgresqlfirewallrule_info
    azure_rm_postgresqlserver:
      redirect: azure.azcollection.azure_rm_postgresqlserver
    azure_rm_postgresqlserver_info:
      redirect: azure.azcollection.azure_rm_postgresqlserver_info
    azure_rm_sqldatabase:
      redirect: azure.azcollection.azure_rm_sqldatabase
    azure_rm_sqldatabase_info:
      redirect: azure.azcollection.azure_rm_sqldatabase_info
    azure_rm_sqlfirewallrule:
      redirect: azure.azcollection.azure_rm_sqlfirewallrule
    azure_rm_sqlfirewallrule_info:
      redirect: azure.azcollection.azure_rm_sqlfirewallrule_info
    azure_rm_sqlserver:
      redirect: azure.azcollection.azure_rm_sqlserver
    azure_rm_sqlserver_info:
      redirect: azure.azcollection.azure_rm_sqlserver_info
    openvswitch_port:
      redirect: openvswitch.openvswitch.openvswitch_port
    openvswitch_db:
      redirect: openvswitch.openvswitch.openvswitch_db
    openvswitch_bridge:
      redirect: openvswitch.openvswitch.openvswitch_bridge
    vyos_ospfv2:
      redirect: vyos.vyos.vyos_ospfv2
    vyos_l3_interface:
      redirect: vyos.vyos.vyos_l3_interface
    vyos_banner:
      redirect: vyos.vyos.vyos_banner
    vyos_firewall_rules:
      redirect: vyos.vyos.vyos_firewall_rules
    vyos_static_route:
      redirect: vyos.vyos.vyos_static_route
    vyos_lldp_interface:
      redirect: vyos.vyos.vyos_lldp_interface
    vyos_vlan:
      redirect: vyos.vyos.vyos_vlan
    vyos_user:
      redirect: vyos.vyos.vyos_user
    vyos_firewall_interfaces:
      redirect: vyos.vyos.vyos_firewall_interfaces
    vyos_interface:
      redirect: vyos.vyos.vyos_interface
    vyos_firewall_global:
      redirect: vyos.vyos.vyos_firewall_global
    vyos_config:
      redirect: vyos.vyos.vyos_config
    vyos_facts:
      redirect: vyos.vyos.vyos_facts
    vyos_linkagg:
      redirect: vyos.vyos.vyos_linkagg
    vyos_ping:
      redirect: vyos.vyos.vyos_ping
    vyos_lag_interfaces:
      redirect: vyos.vyos.vyos_lag_interfaces
    vyos_lldp:
      redirect: vyos.vyos.vyos_lldp
    vyos_lldp_global:
      redirect: vyos.vyos.vyos_lldp_global
    vyos_l3_interfaces:
      redirect: vyos.vyos.vyos_l3_interfaces
    vyos_lldp_interfaces:
      redirect: vyos.vyos.vyos_lldp_interfaces
    vyos_interfaces:
      redirect: vyos.vyos.vyos_interfaces
    vyos_logging:
      redirect: vyos.vyos.vyos_logging
    vyos_static_routes:
      redirect: vyos.vyos.vyos_static_routes
    vyos_command:
      redirect: vyos.vyos.vyos_command
    vyos_system:
      redirect: vyos.vyos.vyos_system
    cpm_plugconfig:
      redirect: wti.remote.cpm_plugconfig
    cpm_plugcontrol:
      redirect: wti.remote.cpm_plugcontrol
    cpm_serial_port_config:
      redirect: wti.remote.cpm_serial_port_config
    cpm_serial_port_info:
      redirect: wti.remote.cpm_serial_port_info
    cpm_user:
      redirect: wti.remote.cpm_user
  module_utils:
    # test entries
    formerly_core:
      redirect: ansible_collections.testns.testcoll.plugins.module_utils.base
    sub1.sub2.formerly_core:
      redirect: ansible_collections.testns.testcoll.plugins.module_utils.base
    # real
    acme:
      redirect: community.crypto.acme
    alicloud_ecs:
      redirect: community.general.alicloud_ecs
    ansible_tower:
      redirect: awx.awx.ansible_tower
    aws.batch:
      redirect: amazon.aws.batch
    aws.cloudfront_facts:
      redirect: amazon.aws.cloudfront_facts
    aws.core:
      redirect: amazon.aws.core
    aws.direct_connect:
      redirect: amazon.aws.direct_connect
    aws.elb_utils:
      redirect: amazon.aws.elb_utils
    aws.elbv2:
      redirect: amazon.aws.elbv2
    aws.iam:
      redirect: amazon.aws.iam
    aws.rds:
      redirect: amazon.aws.rds
    aws.s3:
      redirect: amazon.aws.s3
    aws.urls:
      redirect: amazon.aws.urls
    aws.waf:
      redirect: amazon.aws.waf
    aws.waiters:
      redirect: amazon.aws.waiters
    azure_rm_common:
      redirect: azure.azcollection.azure_rm_common
    azure_rm_common_ext:
      redirect: azure.azcollection.azure_rm_common_ext
    azure_rm_common_rest:
      redirect: azure.azcollection.azure_rm_common_rest
    cloud:
      redirect: community.general.cloud
    cloudscale:
      redirect: cloudscale_ch.cloud.api
    cloudstack:
      redirect: ngine_io.cloudstack.cloudstack
    compat.ipaddress:
      redirect: ansible.netcommon.compat.ipaddress
    crypto:
      redirect: community.crypto.crypto
    database:
      redirect: community.general.database
    digital_ocean:
      redirect: community.digitalocean.digital_ocean
    dimensiondata:
      redirect: community.general.dimensiondata
    docker:
      redirect: community.general.docker
    docker.common:
      redirect: community.general.docker.common
    docker.swarm:
      redirect: community.general.docker.swarm
    ec2:
      redirect: amazon.aws.ec2
    ecs:
      redirect: community.crypto.ecs
    ecs.api:
      redirect: community.crypto.ecs.api
    exoscale:
      redirect: ngine_io.exoscale.exoscale
    f5_utils:
      tombstone:
        removal_date: 2019-11-06
    firewalld:
      redirect: ansible.posix.firewalld
    gcdns:
      redirect: community.general.gcdns
    gce:
      redirect: community.general.gce
    gcp:
      redirect: community.general.gcp
    gcp_utils:
      redirect: google.cloud.gcp_utils
    gitlab:
      redirect: community.general.gitlab
    hcloud:
      redirect: hetzner.hcloud.hcloud
    heroku:
      redirect: community.general.heroku
    hetzner:
      redirect: community.general.hetzner
    hwc_utils:
      redirect: community.general.hwc_utils
    ibm_sa_utils:
      redirect: community.general.ibm_sa_utils
    identity:
      redirect: community.general.identity
    identity.keycloak:
      redirect: community.general.identity.keycloak
    identity.keycloak.keycloak:
      redirect: community.general.identity.keycloak.keycloak
    infinibox:
      redirect: infinidat.infinibox.infinibox
    influxdb:
      redirect: community.general.influxdb
    ipa:
      redirect: community.general.ipa
    ismount:
      redirect: ansible.posix.mount
    k8s.common:
      redirect: community.kubernetes.common
    k8s.raw:
      redirect: community.kubernetes.raw
    k8s.scale:
      redirect: community.kubernetes.scale
    known_hosts:
      redirect: community.general.known_hosts
    kubevirt:
      redirect: community.general.kubevirt
    ldap:
      redirect: community.general.ldap
    linode:
      redirect: community.general.linode
    lxd:
      redirect: community.general.lxd
    manageiq:
      redirect: community.general.manageiq
    memset:
      redirect: community.general.memset
    mysql:
      redirect: community.mysql.mysql
    net_tools.netbox.netbox_utils:
      redirect: netbox.netbox.netbox_utils
    net_tools.nios:
      redirect: community.general.net_tools.nios
    net_tools.nios.api:
      redirect: community.general.net_tools.nios.api
    netapp:
      redirect: netapp.ontap.netapp
    netapp_elementsw_module:
      redirect: netapp.ontap.netapp_elementsw_module
    netapp_module:
      redirect: netapp.ontap.netapp_module
    network.a10.a10:
      redirect: community.network.network.a10.a10
    network.aci.aci:
      redirect: cisco.aci.aci
    network.aci.mso:
      redirect: cisco.mso.mso
    network.aireos.aireos:
      redirect: community.network.network.aireos.aireos
    network.aos.aos:
      redirect: community.network.network.aos.aos
    network.aruba.aruba:
      redirect: community.network.network.aruba.aruba
    network.asa.asa:
      redirect: cisco.asa.network.asa.asa
    network.avi.ansible_utils:
      redirect: community.network.network.avi.ansible_utils
    network.avi.avi:
      redirect: community.network.network.avi.avi
    network.avi.avi_api:
      redirect: community.network.network.avi.avi_api
    network.bigswitch.bigswitch:
      redirect: community.network.network.bigswitch.bigswitch
    network.checkpoint.checkpoint:
      redirect: check_point.mgmt.checkpoint
    network.cloudengine.ce:
      redirect: community.network.network.cloudengine.ce
    network.cnos.cnos:
      redirect: community.network.network.cnos.cnos
    network.cnos.cnos_devicerules:
      redirect: community.network.network.cnos.cnos_devicerules
    network.cnos.cnos_errorcodes:
      redirect: community.network.network.cnos.cnos_errorcodes
    network.common.cfg.base:
      redirect: ansible.netcommon.network.common.cfg.base
    network.common.config:
      redirect: ansible.netcommon.network.common.config
    network.common.facts.facts:
      redirect: ansible.netcommon.network.common.facts.facts
    network.common.netconf:
      redirect: ansible.netcommon.network.common.netconf
    network.common.network:
      redirect: ansible.netcommon.network.common.network
    network.common.parsing:
      redirect: ansible.netcommon.network.common.parsing
    network.common.utils:
      redirect: ansible.netcommon.network.common.utils
    network.dellos10.dellos10:
      redirect: dellemc.os10.network.os10
    network.dellos9.dellos9:
      redirect: dellemc.os9.network.os9
    network.dellos6.dellos6:
      redirect: dellemc.os6.network.os6
    network.edgeos.edgeos:
      redirect: community.network.network.edgeos.edgeos
    network.edgeswitch.edgeswitch:
      redirect: community.network.network.edgeswitch.edgeswitch
    network.edgeswitch.edgeswitch_interface:
      redirect: community.network.network.edgeswitch.edgeswitch_interface
    network.enos.enos:
      redirect: community.network.network.enos.enos
    network.eos.argspec.facts:
      redirect: arista.eos.network.eos.argspec.facts
    network.eos.argspec.facts.facts:
      redirect: arista.eos.network.eos.argspec.facts.facts
    network.eos.argspec.interfaces:
      redirect: arista.eos.network.eos.argspec.interfaces
    network.eos.argspec.interfaces.interfaces:
      redirect: arista.eos.network.eos.argspec.interfaces.interfaces
    network.eos.argspec.l2_interfaces:
      redirect: arista.eos.network.eos.argspec.l2_interfaces
    network.eos.argspec.l2_interfaces.l2_interfaces:
      redirect: arista.eos.network.eos.argspec.l2_interfaces.l2_interfaces
    network.eos.argspec.l3_interfaces:
      redirect: arista.eos.network.eos.argspec.l3_interfaces
    network.eos.argspec.l3_interfaces.l3_interfaces:
      redirect: arista.eos.network.eos.argspec.l3_interfaces.l3_interfaces
    network.eos.argspec.lacp:
      redirect: arista.eos.network.eos.argspec.lacp
    network.eos.argspec.lacp.lacp:
      redirect: arista.eos.network.eos.argspec.lacp.lacp
    network.eos.argspec.lacp_interfaces:
      redirect: arista.eos.network.eos.argspec.lacp_interfaces
    network.eos.argspec.lacp_interfaces.lacp_interfaces:
      redirect: arista.eos.network.eos.argspec.lacp_interfaces.lacp_interfaces
    network.eos.argspec.lag_interfaces:
      redirect: arista.eos.network.eos.argspec.lag_interfaces
    network.eos.argspec.lag_interfaces.lag_interfaces:
      redirect: arista.eos.network.eos.argspec.lag_interfaces.lag_interfaces
    network.eos.argspec.lldp_global:
      redirect: arista.eos.network.eos.argspec.lldp_global
    network.eos.argspec.lldp_global.lldp_global:
      redirect: arista.eos.network.eos.argspec.lldp_global.lldp_global
    network.eos.argspec.lldp_interfaces:
      redirect: arista.eos.network.eos.argspec.lldp_interfaces
    network.eos.argspec.lldp_interfaces.lldp_interfaces:
      redirect: arista.eos.network.eos.argspec.lldp_interfaces.lldp_interfaces
    network.eos.argspec.vlans:
      redirect: arista.eos.network.eos.argspec.vlans
    network.eos.argspec.vlans.vlans:
      redirect: arista.eos.network.eos.argspec.vlans.vlans
    network.eos.config:
      redirect: arista.eos.network.eos.config
    network.eos.config.interfaces:
      redirect: arista.eos.network.eos.config.interfaces
    network.eos.config.interfaces.interfaces:
      redirect: arista.eos.network.eos.config.interfaces.interfaces
    network.eos.config.l2_interfaces:
      redirect: arista.eos.network.eos.config.l2_interfaces
    network.eos.config.l2_interfaces.l2_interfaces:
      redirect: arista.eos.network.eos.config.l2_interfaces.l2_interfaces
    network.eos.config.l3_interfaces:
      redirect: arista.eos.network.eos.config.l3_interfaces
    network.eos.config.l3_interfaces.l3_interfaces:
      redirect: arista.eos.network.eos.config.l3_interfaces.l3_interfaces
    network.eos.config.lacp:
      redirect: arista.eos.network.eos.config.lacp
    network.eos.config.lacp.lacp:
      redirect: arista.eos.network.eos.config.lacp.lacp
    network.eos.config.lacp_interfaces:
      redirect: arista.eos.network.eos.config.lacp_interfaces
    network.eos.config.lacp_interfaces.lacp_interfaces:
      redirect: arista.eos.network.eos.config.lacp_interfaces.lacp_interfaces
    network.eos.config.lag_interfaces:
      redirect: arista.eos.network.eos.config.lag_interfaces
    network.eos.config.lag_interfaces.lag_interfaces:
      redirect: arista.eos.network.eos.config.lag_interfaces.lag_interfaces
    network.eos.config.lldp_global:
      redirect: arista.eos.network.eos.config.lldp_global
    network.eos.config.lldp_global.lldp_global:
      redirect: arista.eos.network.eos.config.lldp_global.lldp_global
    network.eos.config.lldp_interfaces:
      redirect: arista.eos.network.eos.config.lldp_interfaces
    network.eos.config.lldp_interfaces.lldp_interfaces:
      redirect: arista.eos.network.eos.config.lldp_interfaces.lldp_interfaces
    network.eos.config.vlans:
      redirect: arista.eos.network.eos.config.vlans
    network.eos.config.vlans.vlans:
      redirect: arista.eos.network.eos.config.vlans.vlans
    network.eos.eos:
      redirect: arista.eos.network.eos.eos
    network.eos.facts:
      redirect: arista.eos.network.eos.facts
    network.eos.facts.facts:
      redirect: arista.eos.network.eos.facts.facts
    network.eos.facts.interfaces:
      redirect: arista.eos.network.eos.facts.interfaces
    network.eos.facts.interfaces.interfaces:
      redirect: arista.eos.network.eos.facts.interfaces.interfaces
    network.eos.facts.l2_interfaces:
      redirect: arista.eos.network.eos.facts.l2_interfaces
    network.eos.facts.l2_interfaces.l2_interfaces:
      redirect: arista.eos.network.eos.facts.l2_interfaces.l2_interfaces
    network.eos.facts.l3_interfaces:
      redirect: arista.eos.network.eos.facts.l3_interfaces
    network.eos.facts.l3_interfaces.l3_interfaces:
      redirect: arista.eos.network.eos.facts.l3_interfaces.l3_interfaces
    network.eos.facts.lacp:
      redirect: arista.eos.network.eos.facts.lacp
    network.eos.facts.lacp.lacp:
      redirect: arista.eos.network.eos.facts.lacp.lacp
    network.eos.facts.lacp_interfaces:
      redirect: arista.eos.network.eos.facts.lacp_interfaces
    network.eos.facts.lacp_interfaces.lacp_interfaces:
      redirect: arista.eos.network.eos.facts.lacp_interfaces.lacp_interfaces
    network.eos.facts.lag_interfaces:
      redirect: arista.eos.network.eos.facts.lag_interfaces
    network.eos.facts.lag_interfaces.lag_interfaces:
      redirect: arista.eos.network.eos.facts.lag_interfaces.lag_interfaces
    network.eos.facts.legacy:
      redirect: arista.eos.network.eos.facts.legacy
    network.eos.facts.legacy.base:
      redirect: arista.eos.network.eos.facts.legacy.base
    network.eos.facts.lldp_global:
      redirect: arista.eos.network.eos.facts.lldp_global
    network.eos.facts.lldp_global.lldp_global:
      redirect: arista.eos.network.eos.facts.lldp_global.lldp_global
    network.eos.facts.lldp_interfaces:
      redirect: arista.eos.network.eos.facts.lldp_interfaces
    network.eos.facts.lldp_interfaces.lldp_interfaces:
      redirect: arista.eos.network.eos.facts.lldp_interfaces.lldp_interfaces
    network.eos.facts.vlans:
      redirect: arista.eos.network.eos.facts.vlans
    network.eos.facts.vlans.vlans:
      redirect: arista.eos.network.eos.facts.vlans.vlans
    network.eos.providers:
      redirect: arista.eos.network.eos.providers
    network.eos.providers.cli:
      redirect: arista.eos.network.eos.providers.cli
    network.eos.providers.cli.config:
      redirect: arista.eos.network.eos.providers.cli.config
    network.eos.providers.cli.config.bgp:
      redirect: arista.eos.network.eos.providers.cli.config.bgp
    network.eos.providers.cli.config.bgp.address_family:
      redirect: arista.eos.network.eos.providers.cli.config.bgp.address_family
    network.eos.providers.cli.config.bgp.neighbors:
      redirect: arista.eos.network.eos.providers.cli.config.bgp.neighbors
    network.eos.providers.cli.config.bgp.process:
      redirect: arista.eos.network.eos.providers.cli.config.bgp.process
    network.eos.providers.module:
      redirect: arista.eos.network.eos.providers.module
    network.eos.providers.providers:
      redirect: arista.eos.network.eos.providers.providers
    network.eos.utils:
      redirect: arista.eos.network.eos.utils
    network.eos.utils.utils:
      redirect: arista.eos.network.eos.utils.utils
    network.eric_eccli.eric_eccli:
      redirect: community.network.network.eric_eccli.eric_eccli
    network.exos.argspec.facts.facts:
      redirect: community.network.network.exos.argspec.facts.facts
    network.exos.argspec.lldp_global:
      redirect: community.network.network.exos.argspec.lldp_global
    network.exos.argspec.lldp_global.lldp_global:
      redirect: community.network.network.exos.argspec.lldp_global.lldp_global
    network.exos.config.lldp_global:
      redirect: community.network.network.exos.config.lldp_global
    network.exos.config.lldp_global.lldp_global:
      redirect: community.network.network.exos.config.lldp_global.lldp_global
    network.exos.exos:
      redirect: community.network.network.exos.exos
    network.exos.facts.facts:
      redirect: community.network.network.exos.facts.facts
    network.exos.facts.legacy:
      redirect: community.network.network.exos.facts.legacy
    network.exos.facts.legacy.base:
      redirect: community.network.network.exos.facts.legacy.base
    network.exos.facts.lldp_global:
      redirect: community.network.network.exos.facts.lldp_global
    network.exos.facts.lldp_global.lldp_global:
      redirect: community.network.network.exos.facts.lldp_global.lldp_global
    network.exos.utils.utils:
      redirect: community.network.network.exos.utils.utils
    network.f5.bigip:
      redirect: f5networks.f5_modules.bigip
    network.f5.bigiq:
      redirect: f5networks.f5_modules.bigiq
    network.f5.common:
      redirect: f5networks.f5_modules.common
    network.f5.compare:
      redirect: f5networks.f5_modules.compare
    network.f5.icontrol:
      redirect: f5networks.f5_modules.icontrol
    network.f5.ipaddress:
      redirect: f5networks.f5_modules.ipaddress
    # FIXME: missing
    #network.f5.iworkflow:
    #  redirect: f5networks.f5_modules.iworkflow
    #network.f5.legacy:
    #  redirect: f5networks.f5_modules.legacy
    network.f5.urls:
      redirect: f5networks.f5_modules.urls
    network.fortianalyzer.common:
      redirect: community.network.network.fortianalyzer.common
    network.fortianalyzer.fortianalyzer:
      redirect: community.network.network.fortianalyzer.fortianalyzer
    network.fortimanager.common:
      redirect: fortinet.fortimanager.common
    network.fortimanager.fortimanager:
      redirect: fortinet.fortimanager.fortimanager
    network.fortios.argspec:
      redirect: fortinet.fortios.fortios.argspec
    network.fortios.argspec.facts:
      redirect: fortinet.fortios.fortios.argspec.facts
    network.fortios.argspec.facts.facts:
      redirect: fortinet.fortios.fortios.argspec.facts.facts
    network.fortios.argspec.system:
      redirect: fortinet.fortios.fortios.argspec.system
    network.fortios.argspec.system.system:
      redirect: fortinet.fortios.fortios.argspec.system.system
    network.fortios.facts:
      redirect: fortinet.fortios.fortios.facts
    network.fortios.facts.facts:
      redirect: fortinet.fortios.fortios.facts.facts
    network.fortios.facts.system:
      redirect: fortinet.fortios.fortios.facts.system
    network.fortios.facts.system.system:
      redirect: fortinet.fortios.fortios.facts.system.system
    network.fortios.fortios:
      redirect: fortinet.fortios.fortios.fortios
    network.frr:
      redirect: frr.frr.network.frr
    network.frr.frr:
      redirect: frr.frr.network.frr.frr
    network.frr.providers:
      redirect: frr.frr.network.frr.providers
    network.frr.providers.cli:
      redirect: frr.frr.network.frr.providers.cli
    network.frr.providers.cli.config:
      redirect: frr.frr.network.frr.providers.cli.config
    network.frr.providers.cli.config.base:
      redirect: frr.frr.network.frr.providers.cli.config.base
    network.frr.providers.cli.config.bgp:
      redirect: frr.frr.network.frr.providers.cli.config.bgp
    network.frr.providers.cli.config.bgp.address_family:
      redirect: frr.frr.network.frr.providers.cli.config.bgp.address_family
    network.frr.providers.cli.config.bgp.neighbors:
      redirect: frr.frr.network.frr.providers.cli.config.bgp.neighbors
    network.frr.providers.cli.config.bgp.process:
      redirect: frr.frr.network.frr.providers.cli.config.bgp.process
    network.frr.providers.module:
      redirect: frr.frr.network.frr.providers.module
    network.frr.providers.providers:
      redirect: frr.frr.network.frr.providers.providers
    network.ftd:
      redirect: community.network.network.ftd
    network.ftd.common:
      redirect: community.network.network.ftd.common
    network.ftd.configuration:
      redirect: community.network.network.ftd.configuration
    network.ftd.device:
      redirect: community.network.network.ftd.device
    network.ftd.fdm_swagger_client:
      redirect: community.network.network.ftd.fdm_swagger_client
    network.ftd.operation:
      redirect: community.network.network.ftd.operation
    network.icx:
      redirect: community.network.network.icx
    network.icx.icx:
      redirect: community.network.network.icx.icx
    network.ingate:
      redirect: community.network.network.ingate
    network.ingate.common:
      redirect: community.network.network.ingate.common
    network.ios:
      redirect: cisco.ios.network.ios
    network.ios.argspec:
      redirect: cisco.ios.network.ios.argspec
    network.ios.argspec.facts:
      redirect: cisco.ios.network.ios.argspec.facts
    network.ios.argspec.facts.facts:
      redirect: cisco.ios.network.ios.argspec.facts.facts
    network.ios.argspec.interfaces:
      redirect: cisco.ios.network.ios.argspec.interfaces
    network.ios.argspec.interfaces.interfaces:
      redirect: cisco.ios.network.ios.argspec.interfaces.interfaces
    network.ios.argspec.l2_interfaces:
      redirect: cisco.ios.network.ios.argspec.l2_interfaces
    network.ios.argspec.l2_interfaces.l2_interfaces:
      redirect: cisco.ios.network.ios.argspec.l2_interfaces.l2_interfaces
    network.ios.argspec.l3_interfaces:
      redirect: cisco.ios.network.ios.argspec.l3_interfaces
    network.ios.argspec.l3_interfaces.l3_interfaces:
      redirect: cisco.ios.network.ios.argspec.l3_interfaces.l3_interfaces
    network.ios.argspec.lacp:
      redirect: cisco.ios.network.ios.argspec.lacp
    network.ios.argspec.lacp.lacp:
      redirect: cisco.ios.network.ios.argspec.lacp.lacp
    network.ios.argspec.lacp_interfaces:
      redirect: cisco.ios.network.ios.argspec.lacp_interfaces
    network.ios.argspec.lacp_interfaces.lacp_interfaces:
      redirect: cisco.ios.network.ios.argspec.lacp_interfaces.lacp_interfaces
    network.ios.argspec.lag_interfaces:
      redirect: cisco.ios.network.ios.argspec.lag_interfaces
    network.ios.argspec.lag_interfaces.lag_interfaces:
      redirect: cisco.ios.network.ios.argspec.lag_interfaces.lag_interfaces
    network.ios.argspec.lldp_global:
      redirect: cisco.ios.network.ios.argspec.lldp_global
    network.ios.argspec.lldp_global.lldp_global:
      redirect: cisco.ios.network.ios.argspec.lldp_global.lldp_global
    network.ios.argspec.lldp_interfaces:
      redirect: cisco.ios.network.ios.argspec.lldp_interfaces
    network.ios.argspec.lldp_interfaces.lldp_interfaces:
      redirect: cisco.ios.network.ios.argspec.lldp_interfaces.lldp_interfaces
    network.ios.argspec.vlans:
      redirect: cisco.ios.network.ios.argspec.vlans
    network.ios.argspec.vlans.vlans:
      redirect: cisco.ios.network.ios.argspec.vlans.vlans
    network.ios.config:
      redirect: cisco.ios.network.ios.config
    network.ios.config.interfaces:
      redirect: cisco.ios.network.ios.config.interfaces
    network.ios.config.interfaces.interfaces:
      redirect: cisco.ios.network.ios.config.interfaces.interfaces
    network.ios.config.l2_interfaces:
      redirect: cisco.ios.network.ios.config.l2_interfaces
    network.ios.config.l2_interfaces.l2_interfaces:
      redirect: cisco.ios.network.ios.config.l2_interfaces.l2_interfaces
    network.ios.config.l3_interfaces:
      redirect: cisco.ios.network.ios.config.l3_interfaces
    network.ios.config.l3_interfaces.l3_interfaces:
      redirect: cisco.ios.network.ios.config.l3_interfaces.l3_interfaces
    network.ios.config.lacp:
      redirect: cisco.ios.network.ios.config.lacp
    network.ios.config.lacp.lacp:
      redirect: cisco.ios.network.ios.config.lacp.lacp
    network.ios.config.lacp_interfaces:
      redirect: cisco.ios.network.ios.config.lacp_interfaces
    network.ios.config.lacp_interfaces.lacp_interfaces:
      redirect: cisco.ios.network.ios.config.lacp_interfaces.lacp_interfaces
    network.ios.config.lag_interfaces:
      redirect: cisco.ios.network.ios.config.lag_interfaces
    network.ios.config.lag_interfaces.lag_interfaces:
      redirect: cisco.ios.network.ios.config.lag_interfaces.lag_interfaces
    network.ios.config.lldp_global:
      redirect: cisco.ios.network.ios.config.lldp_global
    network.ios.config.lldp_global.lldp_global:
      redirect: cisco.ios.network.ios.config.lldp_global.lldp_global
    network.ios.config.lldp_interfaces:
      redirect: cisco.ios.network.ios.config.lldp_interfaces
    network.ios.config.lldp_interfaces.lldp_interfaces:
      redirect: cisco.ios.network.ios.config.lldp_interfaces.lldp_interfaces
    network.ios.config.vlans:
      redirect: cisco.ios.network.ios.config.vlans
    network.ios.config.vlans.vlans:
      redirect: cisco.ios.network.ios.config.vlans.vlans
    network.ios.facts:
      redirect: cisco.ios.network.ios.facts
    network.ios.facts.facts:
      redirect: cisco.ios.network.ios.facts.facts
    network.ios.facts.interfaces:
      redirect: cisco.ios.network.ios.facts.interfaces
    network.ios.facts.interfaces.interfaces:
      redirect: cisco.ios.network.ios.facts.interfaces.interfaces
    network.ios.facts.l2_interfaces:
      redirect: cisco.ios.network.ios.facts.l2_interfaces
    network.ios.facts.l2_interfaces.l2_interfaces:
      redirect: cisco.ios.network.ios.facts.l2_interfaces.l2_interfaces
    network.ios.facts.l3_interfaces:
      redirect: cisco.ios.network.ios.facts.l3_interfaces
    network.ios.facts.l3_interfaces.l3_interfaces:
      redirect: cisco.ios.network.ios.facts.l3_interfaces.l3_interfaces
    network.ios.facts.lacp:
      redirect: cisco.ios.network.ios.facts.lacp
    network.ios.facts.lacp.lacp:
      redirect: cisco.ios.network.ios.facts.lacp.lacp
    network.ios.facts.lacp_interfaces:
      redirect: cisco.ios.network.ios.facts.lacp_interfaces
    network.ios.facts.lacp_interfaces.lacp_interfaces:
      redirect: cisco.ios.network.ios.facts.lacp_interfaces.lacp_interfaces
    network.ios.facts.lag_interfaces:
      redirect: cisco.ios.network.ios.facts.lag_interfaces
    network.ios.facts.lag_interfaces.lag_interfaces:
      redirect: cisco.ios.network.ios.facts.lag_interfaces.lag_interfaces
    network.ios.facts.legacy:
      redirect: cisco.ios.network.ios.facts.legacy
    network.ios.facts.legacy.base:
      redirect: cisco.ios.network.ios.facts.legacy.base
    network.ios.facts.lldp_global:
      redirect: cisco.ios.network.ios.facts.lldp_global
    network.ios.facts.lldp_global.lldp_global:
      redirect: cisco.ios.network.ios.facts.lldp_global.lldp_global
    network.ios.facts.lldp_interfaces:
      redirect: cisco.ios.network.ios.facts.lldp_interfaces
    network.ios.facts.lldp_interfaces.lldp_interfaces:
      redirect: cisco.ios.network.ios.facts.lldp_interfaces.lldp_interfaces
    network.ios.facts.vlans:
      redirect: cisco.ios.network.ios.facts.vlans
    network.ios.facts.vlans.vlans:
      redirect: cisco.ios.network.ios.facts.vlans.vlans
    network.ios.ios:
      redirect: cisco.ios.network.ios.ios
    network.ios.providers:
      redirect: cisco.ios.network.ios.providers
    network.ios.providers.cli:
      redirect: cisco.ios.network.ios.providers.cli
    network.ios.providers.cli.config:
      redirect: cisco.ios.network.ios.providers.cli.config
    network.ios.providers.cli.config.base:
      redirect: cisco.ios.network.ios.providers.cli.config.base
    network.ios.providers.cli.config.bgp:
      redirect: cisco.ios.network.ios.providers.cli.config.bgp
    network.ios.providers.cli.config.bgp.address_family:
      redirect: cisco.ios.network.ios.providers.cli.config.bgp.address_family
    network.ios.providers.cli.config.bgp.neighbors:
      redirect: cisco.ios.network.ios.providers.cli.config.bgp.neighbors
    network.ios.providers.cli.config.bgp.process:
      redirect: cisco.ios.network.ios.providers.cli.config.bgp.process
    network.ios.providers.module:
      redirect: cisco.ios.network.ios.providers.module
    network.ios.providers.providers:
      redirect: cisco.ios.network.ios.providers.providers
    network.ios.utils:
      redirect: cisco.ios.network.ios.utils
    network.ios.utils.utils:
      redirect: cisco.ios.network.ios.utils.utils
    network.iosxr:
      redirect: cisco.iosxr.network.iosxr
    network.iosxr.argspec:
      redirect: cisco.iosxr.network.iosxr.argspec
    network.iosxr.argspec.facts:
      redirect: cisco.iosxr.network.iosxr.argspec.facts
    network.iosxr.argspec.facts.facts:
      redirect: cisco.iosxr.network.iosxr.argspec.facts.facts
    network.iosxr.argspec.interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.interfaces
    network.iosxr.argspec.interfaces.interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.interfaces.interfaces
    network.iosxr.argspec.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.l2_interfaces
    network.iosxr.argspec.l2_interfaces.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.l2_interfaces.l2_interfaces
    network.iosxr.argspec.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.l3_interfaces
    network.iosxr.argspec.l3_interfaces.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.l3_interfaces.l3_interfaces
    network.iosxr.argspec.lacp:
      redirect: cisco.iosxr.network.iosxr.argspec.lacp
    network.iosxr.argspec.lacp.lacp:
      redirect: cisco.iosxr.network.iosxr.argspec.lacp.lacp
    network.iosxr.argspec.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lacp_interfaces
    network.iosxr.argspec.lacp_interfaces.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lacp_interfaces.lacp_interfaces
    network.iosxr.argspec.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lag_interfaces
    network.iosxr.argspec.lag_interfaces.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lag_interfaces.lag_interfaces
    network.iosxr.argspec.lldp_global:
      redirect: cisco.iosxr.network.iosxr.argspec.lldp_global
    network.iosxr.argspec.lldp_global.lldp_global:
      redirect: cisco.iosxr.network.iosxr.argspec.lldp_global.lldp_global
    network.iosxr.argspec.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lldp_interfaces
    network.iosxr.argspec.lldp_interfaces.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.argspec.lldp_interfaces.lldp_interfaces
    network.iosxr.config:
      redirect: cisco.iosxr.network.iosxr.config
    network.iosxr.config.interfaces:
      redirect: cisco.iosxr.network.iosxr.config.interfaces
    network.iosxr.config.interfaces.interfaces:
      redirect: cisco.iosxr.network.iosxr.config.interfaces.interfaces
    network.iosxr.config.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.l2_interfaces
    network.iosxr.config.l2_interfaces.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.l2_interfaces.l2_interfaces
    network.iosxr.config.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.l3_interfaces
    network.iosxr.config.l3_interfaces.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.l3_interfaces.l3_interfaces
    network.iosxr.config.lacp:
      redirect: cisco.iosxr.network.iosxr.config.lacp
    network.iosxr.config.lacp.lacp:
      redirect: cisco.iosxr.network.iosxr.config.lacp.lacp
    network.iosxr.config.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lacp_interfaces
    network.iosxr.config.lacp_interfaces.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lacp_interfaces.lacp_interfaces
    network.iosxr.config.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lag_interfaces
    network.iosxr.config.lag_interfaces.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lag_interfaces.lag_interfaces
    network.iosxr.config.lldp_global:
      redirect: cisco.iosxr.network.iosxr.config.lldp_global
    network.iosxr.config.lldp_global.lldp_global:
      redirect: cisco.iosxr.network.iosxr.config.lldp_global.lldp_global
    network.iosxr.config.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lldp_interfaces
    network.iosxr.config.lldp_interfaces.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.config.lldp_interfaces.lldp_interfaces
    network.iosxr.facts:
      redirect: cisco.iosxr.network.iosxr.facts
    network.iosxr.facts.facts:
      redirect: cisco.iosxr.network.iosxr.facts.facts
    network.iosxr.facts.interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.interfaces
    network.iosxr.facts.interfaces.interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.interfaces.interfaces
    network.iosxr.facts.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.l2_interfaces
    network.iosxr.facts.l2_interfaces.l2_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.l2_interfaces.l2_interfaces
    network.iosxr.facts.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.l3_interfaces
    network.iosxr.facts.l3_interfaces.l3_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.l3_interfaces.l3_interfaces
    network.iosxr.facts.lacp:
      redirect: cisco.iosxr.network.iosxr.facts.lacp
    network.iosxr.facts.lacp.lacp:
      redirect: cisco.iosxr.network.iosxr.facts.lacp.lacp
    network.iosxr.facts.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lacp_interfaces
    network.iosxr.facts.lacp_interfaces.lacp_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lacp_interfaces.lacp_interfaces
    network.iosxr.facts.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lag_interfaces
    network.iosxr.facts.lag_interfaces.lag_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lag_interfaces.lag_interfaces
    network.iosxr.facts.legacy:
      redirect: cisco.iosxr.network.iosxr.facts.legacy
    network.iosxr.facts.legacy.base:
      redirect: cisco.iosxr.network.iosxr.facts.legacy.base
    network.iosxr.facts.lldp_global:
      redirect: cisco.iosxr.network.iosxr.facts.lldp_global
    network.iosxr.facts.lldp_global.lldp_global:
      redirect: cisco.iosxr.network.iosxr.facts.lldp_global.lldp_global
    network.iosxr.facts.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lldp_interfaces
    network.iosxr.facts.lldp_interfaces.lldp_interfaces:
      redirect: cisco.iosxr.network.iosxr.facts.lldp_interfaces.lldp_interfaces
    network.iosxr.iosxr:
      redirect: cisco.iosxr.network.iosxr.iosxr
    network.iosxr.providers:
      redirect: cisco.iosxr.network.iosxr.providers
    network.iosxr.providers.cli:
      redirect: cisco.iosxr.network.iosxr.providers.cli
    network.iosxr.providers.cli.config:
      redirect: cisco.iosxr.network.iosxr.providers.cli.config
    network.iosxr.providers.cli.config.bgp:
      redirect: cisco.iosxr.network.iosxr.providers.cli.config.bgp
    network.iosxr.providers.cli.config.bgp.address_family:
      redirect: cisco.iosxr.network.iosxr.providers.cli.config.bgp.address_family
    network.iosxr.providers.cli.config.bgp.neighbors:
      redirect: cisco.iosxr.network.iosxr.providers.cli.config.bgp.neighbors
    network.iosxr.providers.cli.config.bgp.process:
      redirect: cisco.iosxr.network.iosxr.providers.cli.config.bgp.process
    network.iosxr.providers.module:
      redirect: cisco.iosxr.network.iosxr.providers.module
    network.iosxr.providers.providers:
      redirect: cisco.iosxr.network.iosxr.providers.providers
    network.iosxr.utils:
      redirect: cisco.iosxr.network.iosxr.utils
    network.iosxr.utils.utils:
      redirect: cisco.iosxr.network.iosxr.utils.utils
    network.ironware:
      redirect: community.network.network.ironware
    network.ironware.ironware:
      redirect: community.network.network.ironware.ironware
    network.junos:
      redirect: junipernetworks.junos.network.junos
    network.junos.argspec:
      redirect: junipernetworks.junos.network.junos.argspec
    network.junos.argspec.facts:
      redirect: junipernetworks.junos.network.junos.argspec.facts
    network.junos.argspec.facts.facts:
      redirect: junipernetworks.junos.network.junos.argspec.facts.facts
    network.junos.argspec.interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.interfaces
    network.junos.argspec.interfaces.interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.interfaces.interfaces
    network.junos.argspec.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.l2_interfaces
    network.junos.argspec.l2_interfaces.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.l2_interfaces.l2_interfaces
    network.junos.argspec.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.l3_interfaces
    network.junos.argspec.l3_interfaces.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.l3_interfaces.l3_interfaces
    network.junos.argspec.lacp:
      redirect: junipernetworks.junos.network.junos.argspec.lacp
    network.junos.argspec.lacp.lacp:
      redirect: junipernetworks.junos.network.junos.argspec.lacp.lacp
    network.junos.argspec.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lacp_interfaces
    network.junos.argspec.lacp_interfaces.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lacp_interfaces.lacp_interfaces
    network.junos.argspec.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lag_interfaces
    network.junos.argspec.lag_interfaces.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lag_interfaces.lag_interfaces
    network.junos.argspec.lldp_global:
      redirect: junipernetworks.junos.network.junos.argspec.lldp_global
    network.junos.argspec.lldp_global.lldp_global:
      redirect: junipernetworks.junos.network.junos.argspec.lldp_global.lldp_global
    network.junos.argspec.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lldp_interfaces
    network.junos.argspec.lldp_interfaces.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.argspec.lldp_interfaces.lldp_interfaces
    network.junos.argspec.vlans:
      redirect: junipernetworks.junos.network.junos.argspec.vlans
    network.junos.argspec.vlans.vlans:
      redirect: junipernetworks.junos.network.junos.argspec.vlans.vlans
    network.junos.config:
      redirect: junipernetworks.junos.network.junos.config
    network.junos.config.interfaces:
      redirect: junipernetworks.junos.network.junos.config.interfaces
    network.junos.config.interfaces.interfaces:
      redirect: junipernetworks.junos.network.junos.config.interfaces.interfaces
    network.junos.config.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.config.l2_interfaces
    network.junos.config.l2_interfaces.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.config.l2_interfaces.l2_interfaces
    network.junos.config.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.config.l3_interfaces
    network.junos.config.l3_interfaces.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.config.l3_interfaces.l3_interfaces
    network.junos.config.lacp:
      redirect: junipernetworks.junos.network.junos.config.lacp
    network.junos.config.lacp.lacp:
      redirect: junipernetworks.junos.network.junos.config.lacp.lacp
    network.junos.config.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lacp_interfaces
    network.junos.config.lacp_interfaces.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lacp_interfaces.lacp_interfaces
    network.junos.config.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lag_interfaces
    network.junos.config.lag_interfaces.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lag_interfaces.lag_interfaces
    network.junos.config.lldp_global:
      redirect: junipernetworks.junos.network.junos.config.lldp_global
    network.junos.config.lldp_global.lldp_global:
      redirect: junipernetworks.junos.network.junos.config.lldp_global.lldp_global
    network.junos.config.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lldp_interfaces
    network.junos.config.lldp_interfaces.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.config.lldp_interfaces.lldp_interfaces
    network.junos.config.vlans:
      redirect: junipernetworks.junos.network.junos.config.vlans
    network.junos.config.vlans.vlans:
      redirect: junipernetworks.junos.network.junos.config.vlans.vlans
    network.junos.facts:
      redirect: junipernetworks.junos.network.junos.facts
    network.junos.facts.facts:
      redirect: junipernetworks.junos.network.junos.facts.facts
    network.junos.facts.interfaces:
      redirect: junipernetworks.junos.network.junos.facts.interfaces
    network.junos.facts.interfaces.interfaces:
      redirect: junipernetworks.junos.network.junos.facts.interfaces.interfaces
    network.junos.facts.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.l2_interfaces
    network.junos.facts.l2_interfaces.l2_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.l2_interfaces.l2_interfaces
    network.junos.facts.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.l3_interfaces
    network.junos.facts.l3_interfaces.l3_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.l3_interfaces.l3_interfaces
    network.junos.facts.lacp:
      redirect: junipernetworks.junos.network.junos.facts.lacp
    network.junos.facts.lacp.lacp:
      redirect: junipernetworks.junos.network.junos.facts.lacp.lacp
    network.junos.facts.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lacp_interfaces
    network.junos.facts.lacp_interfaces.lacp_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lacp_interfaces.lacp_interfaces
    network.junos.facts.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lag_interfaces
    network.junos.facts.lag_interfaces.lag_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lag_interfaces.lag_interfaces
    network.junos.facts.legacy:
      redirect: junipernetworks.junos.network.junos.facts.legacy
    network.junos.facts.legacy.base:
      redirect: junipernetworks.junos.network.junos.facts.legacy.base
    network.junos.facts.lldp_global:
      redirect: junipernetworks.junos.network.junos.facts.lldp_global
    network.junos.facts.lldp_global.lldp_global:
      redirect: junipernetworks.junos.network.junos.facts.lldp_global.lldp_global
    network.junos.facts.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lldp_interfaces
    network.junos.facts.lldp_interfaces.lldp_interfaces:
      redirect: junipernetworks.junos.network.junos.facts.lldp_interfaces.lldp_interfaces
    network.junos.facts.vlans:
      redirect: junipernetworks.junos.network.junos.facts.vlans
    network.junos.facts.vlans.vlans:
      redirect: junipernetworks.junos.network.junos.facts.vlans.vlans
    network.junos.junos:
      redirect: junipernetworks.junos.network.junos.junos
    network.junos.utils:
      redirect: junipernetworks.junos.network.junos.utils
    network.junos.utils.utils:
      redirect: junipernetworks.junos.network.junos.utils.utils
    network.meraki:
      redirect: cisco.meraki.network.meraki
    network.meraki.meraki:
      redirect: cisco.meraki.network.meraki.meraki
    network.netconf:
      redirect: ansible.netcommon.network.netconf
    network.netconf.netconf:
      redirect: ansible.netcommon.network.netconf.netconf
    network.netscaler:
      redirect: community.network.network.netscaler
    network.netscaler.netscaler:
      redirect: community.network.network.netscaler.netscaler
    network.netvisor:
      redirect: community.network.network.netvisor
    network.netvisor.netvisor:
      redirect: community.network.network.netvisor.netvisor
    network.netvisor.pn_nvos:
      redirect: community.network.network.netvisor.pn_nvos
    network.nos:
      redirect: community.network.network.nos
    network.nos.nos:
      redirect: community.network.network.nos.nos
    network.nso:
      redirect: community.network.network.nso
    network.nso.nso:
      redirect: community.network.network.nso.nso
    network.nxos:
      redirect: cisco.nxos.network.nxos
    network.nxos.argspec:
      redirect: cisco.nxos.network.nxos.argspec
    network.nxos.argspec.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.bfd_interfaces
    network.nxos.argspec.bfd_interfaces.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.bfd_interfaces.bfd_interfaces
    network.nxos.argspec.facts:
      redirect: cisco.nxos.network.nxos.argspec.facts
    network.nxos.argspec.facts.facts:
      redirect: cisco.nxos.network.nxos.argspec.facts.facts
    network.nxos.argspec.interfaces:
      redirect: cisco.nxos.network.nxos.argspec.interfaces
    network.nxos.argspec.interfaces.interfaces:
      redirect: cisco.nxos.network.nxos.argspec.interfaces.interfaces
    network.nxos.argspec.l2_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.l2_interfaces
    network.nxos.argspec.l2_interfaces.l2_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.l2_interfaces.l2_interfaces
    network.nxos.argspec.l3_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.l3_interfaces
    network.nxos.argspec.l3_interfaces.l3_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.l3_interfaces.l3_interfaces
    network.nxos.argspec.lacp:
      redirect: cisco.nxos.network.nxos.argspec.lacp
    network.nxos.argspec.lacp.lacp:
      redirect: cisco.nxos.network.nxos.argspec.lacp.lacp
    network.nxos.argspec.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.lacp_interfaces
    network.nxos.argspec.lacp_interfaces.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.lacp_interfaces.lacp_interfaces
    network.nxos.argspec.lag_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.lag_interfaces
    network.nxos.argspec.lag_interfaces.lag_interfaces:
      redirect: cisco.nxos.network.nxos.argspec.lag_interfaces.lag_interfaces
    network.nxos.argspec.lldp_global:
      redirect: cisco.nxos.network.nxos.argspec.lldp_global
    network.nxos.argspec.lldp_global.lldp_global:
      redirect: cisco.nxos.network.nxos.argspec.lldp_global.lldp_global
    network.nxos.argspec.telemetry:
      redirect: cisco.nxos.network.nxos.argspec.telemetry
    network.nxos.argspec.telemetry.telemetry:
      redirect: cisco.nxos.network.nxos.argspec.telemetry.telemetry
    network.nxos.argspec.vlans:
      redirect: cisco.nxos.network.nxos.argspec.vlans
    network.nxos.argspec.vlans.vlans:
      redirect: cisco.nxos.network.nxos.argspec.vlans.vlans
    network.nxos.cmdref:
      redirect: cisco.nxos.network.nxos.cmdref
    network.nxos.cmdref.telemetry:
      redirect: cisco.nxos.network.nxos.cmdref.telemetry
    network.nxos.cmdref.telemetry.telemetry:
      redirect: cisco.nxos.network.nxos.cmdref.telemetry.telemetry
    network.nxos.config:
      redirect: cisco.nxos.network.nxos.config
    network.nxos.config.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.config.bfd_interfaces
    network.nxos.config.bfd_interfaces.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.config.bfd_interfaces.bfd_interfaces
    network.nxos.config.interfaces:
      redirect: cisco.nxos.network.nxos.config.interfaces
    network.nxos.config.interfaces.interfaces:
      redirect: cisco.nxos.network.nxos.config.interfaces.interfaces
    network.nxos.config.l2_interfaces:
      redirect: cisco.nxos.network.nxos.config.l2_interfaces
    network.nxos.config.l2_interfaces.l2_interfaces:
      redirect: cisco.nxos.network.nxos.config.l2_interfaces.l2_interfaces
    network.nxos.config.l3_interfaces:
      redirect: cisco.nxos.network.nxos.config.l3_interfaces
    network.nxos.config.l3_interfaces.l3_interfaces:
      redirect: cisco.nxos.network.nxos.config.l3_interfaces.l3_interfaces
    network.nxos.config.lacp:
      redirect: cisco.nxos.network.nxos.config.lacp
    network.nxos.config.lacp.lacp:
      redirect: cisco.nxos.network.nxos.config.lacp.lacp
    network.nxos.config.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.config.lacp_interfaces
    network.nxos.config.lacp_interfaces.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.config.lacp_interfaces.lacp_interfaces
    network.nxos.config.lag_interfaces:
      redirect: cisco.nxos.network.nxos.config.lag_interfaces
    network.nxos.config.lag_interfaces.lag_interfaces:
      redirect: cisco.nxos.network.nxos.config.lag_interfaces.lag_interfaces
    network.nxos.config.lldp_global:
      redirect: cisco.nxos.network.nxos.config.lldp_global
    network.nxos.config.lldp_global.lldp_global:
      redirect: cisco.nxos.network.nxos.config.lldp_global.lldp_global
    network.nxos.config.telemetry:
      redirect: cisco.nxos.network.nxos.config.telemetry
    network.nxos.config.telemetry.telemetry:
      redirect: cisco.nxos.network.nxos.config.telemetry.telemetry
    network.nxos.config.vlans:
      redirect: cisco.nxos.network.nxos.config.vlans
    network.nxos.config.vlans.vlans:
      redirect: cisco.nxos.network.nxos.config.vlans.vlans
    network.nxos.facts:
      redirect: cisco.nxos.network.nxos.facts
    network.nxos.facts.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.facts.bfd_interfaces
    network.nxos.facts.bfd_interfaces.bfd_interfaces:
      redirect: cisco.nxos.network.nxos.facts.bfd_interfaces.bfd_interfaces
    network.nxos.facts.facts:
      redirect: cisco.nxos.network.nxos.facts.facts
    network.nxos.facts.interfaces:
      redirect: cisco.nxos.network.nxos.facts.interfaces
    network.nxos.facts.interfaces.interfaces:
      redirect: cisco.nxos.network.nxos.facts.interfaces.interfaces
    network.nxos.facts.l2_interfaces:
      redirect: cisco.nxos.network.nxos.facts.l2_interfaces
    network.nxos.facts.l2_interfaces.l2_interfaces:
      redirect: cisco.nxos.network.nxos.facts.l2_interfaces.l2_interfaces
    network.nxos.facts.l3_interfaces:
      redirect: cisco.nxos.network.nxos.facts.l3_interfaces
    network.nxos.facts.l3_interfaces.l3_interfaces:
      redirect: cisco.nxos.network.nxos.facts.l3_interfaces.l3_interfaces
    network.nxos.facts.lacp:
      redirect: cisco.nxos.network.nxos.facts.lacp
    network.nxos.facts.lacp.lacp:
      redirect: cisco.nxos.network.nxos.facts.lacp.lacp
    network.nxos.facts.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.facts.lacp_interfaces
    network.nxos.facts.lacp_interfaces.lacp_interfaces:
      redirect: cisco.nxos.network.nxos.facts.lacp_interfaces.lacp_interfaces
    network.nxos.facts.lag_interfaces:
      redirect: cisco.nxos.network.nxos.facts.lag_interfaces
    network.nxos.facts.lag_interfaces.lag_interfaces:
      redirect: cisco.nxos.network.nxos.facts.lag_interfaces.lag_interfaces
    network.nxos.facts.legacy:
      redirect: cisco.nxos.network.nxos.facts.legacy
    network.nxos.facts.legacy.base:
      redirect: cisco.nxos.network.nxos.facts.legacy.base
    network.nxos.facts.lldp_global:
      redirect: cisco.nxos.network.nxos.facts.lldp_global
    network.nxos.facts.lldp_global.lldp_global:
      redirect: cisco.nxos.network.nxos.facts.lldp_global.lldp_global
    network.nxos.facts.telemetry:
      redirect: cisco.nxos.network.nxos.facts.telemetry
    network.nxos.facts.telemetry.telemetry:
      redirect: cisco.nxos.network.nxos.facts.telemetry.telemetry
    network.nxos.facts.vlans:
      redirect: cisco.nxos.network.nxos.facts.vlans
    network.nxos.facts.vlans.vlans:
      redirect: cisco.nxos.network.nxos.facts.vlans.vlans
    network.nxos.nxos:
      redirect: cisco.nxos.network.nxos.nxos
    network.nxos.utils:
      redirect: cisco.nxos.network.nxos.utils
    network.nxos.utils.telemetry:
      redirect: cisco.nxos.network.nxos.utils.telemetry
    network.nxos.utils.telemetry.telemetry:
      redirect: cisco.nxos.network.nxos.utils.telemetry.telemetry
    network.nxos.utils.utils:
      redirect: cisco.nxos.network.nxos.utils.utils
    network.onyx:
      redirect: mellanox.onyx.network.onyx
    network.onyx.onyx:
      redirect: mellanox.onyx.network.onyx.onyx
    network.ordnance:
      redirect: community.network.network.ordnance
    network.ordnance.ordnance:
      redirect: community.network.network.ordnance.ordnance
    network.panos:
      redirect: community.network.network.panos
    network.panos.panos:
      redirect: community.network.network.panos.panos
    network.restconf:
      redirect: ansible.netcommon.network.restconf
    network.restconf.restconf:
      redirect: ansible.netcommon.network.restconf.restconf
    network.routeros:
      redirect: community.network.network.routeros
    network.routeros.routeros:
      redirect: community.network.network.routeros.routeros
    network.skydive:
      redirect: community.skydive.network.skydive
    network.skydive.api:
      redirect: community.skydive.network.skydive.api
    network.slxos:
      redirect: community.network.network.slxos
    network.slxos.slxos:
      redirect: community.network.network.slxos.slxos
    network.sros:
      redirect: community.network.network.sros
    network.sros.sros:
      redirect: community.network.network.sros.sros
    network.voss:
      redirect: community.network.network.voss
    network.voss.voss:
      redirect: community.network.network.voss.voss
    network.vyos:
      redirect: vyos.vyos.network.vyos
    network.vyos.argspec:
      redirect: vyos.vyos.network.vyos.argspec
    network.vyos.argspec.facts:
      redirect: vyos.vyos.network.vyos.argspec.facts
    network.vyos.argspec.facts.facts:
      redirect: vyos.vyos.network.vyos.argspec.facts.facts
    network.vyos.argspec.interfaces:
      redirect: vyos.vyos.network.vyos.argspec.interfaces
    network.vyos.argspec.interfaces.interfaces:
      redirect: vyos.vyos.network.vyos.argspec.interfaces.interfaces
    network.vyos.argspec.l3_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.l3_interfaces
    network.vyos.argspec.l3_interfaces.l3_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.l3_interfaces.l3_interfaces
    network.vyos.argspec.lag_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.lag_interfaces
    network.vyos.argspec.lag_interfaces.lag_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.lag_interfaces.lag_interfaces
    network.vyos.argspec.lldp_global:
      redirect: vyos.vyos.network.vyos.argspec.lldp_global
    network.vyos.argspec.lldp_global.lldp_global:
      redirect: vyos.vyos.network.vyos.argspec.lldp_global.lldp_global
    network.vyos.argspec.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.lldp_interfaces
    network.vyos.argspec.lldp_interfaces.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.argspec.lldp_interfaces.lldp_interfaces
    network.vyos.config:
      redirect: vyos.vyos.network.vyos.config
    network.vyos.config.interfaces:
      redirect: vyos.vyos.network.vyos.config.interfaces
    network.vyos.config.interfaces.interfaces:
      redirect: vyos.vyos.network.vyos.config.interfaces.interfaces
    network.vyos.config.l3_interfaces:
      redirect: vyos.vyos.network.vyos.config.l3_interfaces
    network.vyos.config.l3_interfaces.l3_interfaces:
      redirect: vyos.vyos.network.vyos.config.l3_interfaces.l3_interfaces
    network.vyos.config.lag_interfaces:
      redirect: vyos.vyos.network.vyos.config.lag_interfaces
    network.vyos.config.lag_interfaces.lag_interfaces:
      redirect: vyos.vyos.network.vyos.config.lag_interfaces.lag_interfaces
    network.vyos.config.lldp_global:
      redirect: vyos.vyos.network.vyos.config.lldp_global
    network.vyos.config.lldp_global.lldp_global:
      redirect: vyos.vyos.network.vyos.config.lldp_global.lldp_global
    network.vyos.config.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.config.lldp_interfaces
    network.vyos.config.lldp_interfaces.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.config.lldp_interfaces.lldp_interfaces
    network.vyos.facts:
      redirect: vyos.vyos.network.vyos.facts
    network.vyos.facts.facts:
      redirect: vyos.vyos.network.vyos.facts.facts
    network.vyos.facts.interfaces:
      redirect: vyos.vyos.network.vyos.facts.interfaces
    network.vyos.facts.interfaces.interfaces:
      redirect: vyos.vyos.network.vyos.facts.interfaces.interfaces
    network.vyos.facts.l3_interfaces:
      redirect: vyos.vyos.network.vyos.facts.l3_interfaces
    network.vyos.facts.l3_interfaces.l3_interfaces:
      redirect: vyos.vyos.network.vyos.facts.l3_interfaces.l3_interfaces
    network.vyos.facts.lag_interfaces:
      redirect: vyos.vyos.network.vyos.facts.lag_interfaces
    network.vyos.facts.lag_interfaces.lag_interfaces:
      redirect: vyos.vyos.network.vyos.facts.lag_interfaces.lag_interfaces
    network.vyos.facts.legacy:
      redirect: vyos.vyos.network.vyos.facts.legacy
    network.vyos.facts.legacy.base:
      redirect: vyos.vyos.network.vyos.facts.legacy.base
    network.vyos.facts.lldp_global:
      redirect: vyos.vyos.network.vyos.facts.lldp_global
    network.vyos.facts.lldp_global.lldp_global:
      redirect: vyos.vyos.network.vyos.facts.lldp_global.lldp_global
    network.vyos.facts.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.facts.lldp_interfaces
    network.vyos.facts.lldp_interfaces.lldp_interfaces:
      redirect: vyos.vyos.network.vyos.facts.lldp_interfaces.lldp_interfaces
    network.vyos.utils:
      redirect: vyos.vyos.network.vyos.utils
    network.vyos.utils.utils:
      redirect: vyos.vyos.network.vyos.utils.utils
    network.vyos.vyos:
      redirect: vyos.vyos.network.vyos.vyos
    oneandone:
      redirect: community.general.oneandone
    oneview:
      redirect: community.general.oneview
    online:
      redirect: community.general.online
    opennebula:
      redirect: community.general.opennebula
    openstack:
      redirect: openstack.cloud.openstack
    oracle:
      redirect: community.general.oracle
    oracle.oci_utils:
      redirect: community.general.oracle.oci_utils
    ovirt:
      redirect: community.general._ovirt
    podman:
      redirect: containers.podman.podman
    podman.common:
      redirect: containers.podman.podman.common
    postgres:
      redirect: community.general.postgres
    pure:
      redirect: community.general.pure
    rabbitmq:
      redirect: community.rabbitmq.rabbitmq
    rax:
      redirect: community.general.rax
    redfish_utils:
      redirect: community.general.redfish_utils
    redhat:
      redirect: community.general.redhat
    remote_management.dellemc:
      redirect: community.general.remote_management.dellemc
    remote_management.dellemc.dellemc_idrac:
      redirect: community.general.remote_management.dellemc.dellemc_idrac
    remote_management.dellemc.ome:
      redirect: community.general.remote_management.dellemc.ome
    remote_management.intersight:
      redirect: cisco.intersight.intersight
    remote_management.lxca:
      redirect: community.general.remote_management.lxca
    remote_management.lxca.common:
      redirect: community.general.remote_management.lxca.common
    remote_management.ucs:
      redirect: cisco.ucs.ucs
    scaleway:
      redirect: community.general.scaleway
    service_now:
      redirect: servicenow.servicenow.service_now
    source_control:
      redirect: community.general.source_control
    source_control.bitbucket:
      redirect: community.general.source_control.bitbucket
    storage:
      redirect: community.general.storage
    storage.emc:
      redirect: community.general.storage.emc
    storage.emc.emc_vnx:
      redirect: community.general.storage.emc.emc_vnx
    storage.hpe3par:
      redirect: community.general.storage.hpe3par
    storage.hpe3par.hpe3par:
      redirect: community.general.storage.hpe3par.hpe3par
    univention_umc:
      redirect: community.general.univention_umc
    utm_utils:
      redirect: community.general.utm_utils
    vca:
      redirect: community.vmware.vca
    vexata:
      redirect: community.general.vexata
    vmware:
      redirect: community.vmware.vmware
    vmware_rest_client:
      redirect: community.vmware.vmware_rest_client
    vmware_spbm:
      redirect: community.vmware.vmware_spbm
    vultr:
      redirect: ngine_io.vultr.vultr
    xenserver:
      redirect: community.general.xenserver
    # end module_utils
  cliconf:
    frr:
      redirect: frr.frr.frr
    aireos:
      redirect: community.network.aireos
    apconos:
      redirect: community.network.apconos
    aruba:
      redirect: community.network.aruba
    ce:
      redirect: community.network.ce
    cnos:
      redirect: community.network.cnos
    edgeos:
      redirect: community.network.edgeos
    edgeswitch:
      redirect: community.network.edgeswitch
    enos:
      redirect: community.network.enos
    eric_eccli:
      redirect: community.network.eric_eccli
    exos:
      redirect: community.network.exos
    icx:
      redirect: community.network.icx
    ironware:
      redirect: community.network.ironware
    netvisor:
      redirect: community.network.netvisor
    nos:
      redirect: community.network.nos
    onyx:
      redirect: mellanox.onyx.onyx
    routeros:
      redirect: community.network.routeros
    slxos:
      redirect: community.network.slxos
    voss:
      redirect: community.network.voss
    eos:
      redirect: arista.eos.eos
    asa:
      redirect: cisco.asa.asa
    ios:
      redirect: cisco.ios.ios
    iosxr:
      redirect: cisco.iosxr.iosxr
    nxos:
      redirect: cisco.nxos.nxos
    junos:
      redirect: junipernetworks.junos.junos
    dellos10:
      redirect: dellemc.os10.os10
    dellos9:
      redirect: dellemc.os9.os9
    dellos6:
      redirect: dellemc.os6.os6
    vyos:
      redirect: vyos.vyos.vyos
  terminal:
    frr:
      redirect: frr.frr.frr
    aireos:
      redirect: community.network.aireos
    apconos:
      redirect: community.network.apconos
    aruba:
      redirect: community.network.aruba
    ce:
      redirect: community.network.ce
    cnos:
      redirect: community.network.cnos
    edgeos:
      redirect: community.network.edgeos
    edgeswitch:
      redirect: community.network.edgeswitch
    enos:
      redirect: community.network.enos
    eric_eccli:
      redirect: community.network.eric_eccli
    exos:
      redirect: community.network.exos
    icx:
      redirect: community.network.icx
    ironware:
      redirect: community.network.ironware
    netvisor:
      redirect: community.network.netvisor
    nos:
      redirect: community.network.nos
    onyx:
      redirect: mellanox.onyx.onyx
    routeros:
      redirect: community.network.routeros
    slxos:
      redirect: community.network.slxos
    sros:
      redirect: community.network.sros
    voss:
      redirect: community.network.voss
    eos:
      redirect: arista.eos.eos
    asa:
      redirect: cisco.asa.asa
    ios:
      redirect: cisco.ios.ios
    iosxr:
      redirect: cisco.iosxr.iosxr
    nxos:
      redirect: cisco.nxos.nxos
    bigip:
      redirect: f5networks.f5_modules.bigip
    junos:
      redirect: junipernetworks.junos.junos
    dellos10:
      redirect: dellemc.os10.os10
    dellos9:
      redirect: dellemc.os9.os9
    dellos6:
      redirect: dellemc.os6.os6
    vyos:
      redirect: vyos.vyos.vyos
  action:
    # test entry, overloaded with module of same name to use a different base action (ie not "normal.py")
    uses_redirected_action:
      redirect: testns.testcoll.subclassed_norm
    aireos:
      redirect: community.network.aireos
    aruba:
      redirect: community.network.aruba
    ce:
      redirect: community.network.ce
    ce_template:
      redirect: community.network.ce_template
    cnos:
      redirect: community.network.cnos
    edgeos_config:
      redirect: community.network.edgeos_config
    enos:
      redirect: community.network.enos
    exos:
      redirect: community.network.exos
    ironware:
      redirect: community.network.ironware
    nos_config:
      redirect: community.network.nos_config
    onyx_config:
      redirect: mellanox.onyx.onyx_config
    slxos:
      redirect: community.network.slxos
    sros:
      redirect: community.network.sros
    voss:
      redirect: community.network.voss
    aws_s3:
      redirect: amazon.aws.aws_s3
    cli_command:
      redirect: ansible.netcommon.cli_command
    cli_config:
      redirect: ansible.netcommon.cli_config
    net_base:
      redirect: ansible.netcommon.net_base
    net_user:
      redirect: ansible.netcommon.net_user
    net_vlan:
      redirect: ansible.netcommon.net_vlan
    net_static_route:
      redirect: ansible.netcommon.net_static_route
    net_lldp:
      redirect: ansible.netcommon.net_lldp
    net_vrf:
      redirect: ansible.netcommon.net_vrf
    net_ping:
      redirect: ansible.netcommon.net_ping
    net_l3_interface:
      redirect: ansible.netcommon.net_l3_interface
    net_l2_interface:
      redirect: ansible.netcommon.net_l2_interface
    net_interface:
      redirect: ansible.netcommon.net_interface
    net_system:
      redirect: ansible.netcommon.net_system
    net_lldp_interface:
      redirect: ansible.netcommon.net_lldp_interface
    net_put:
      redirect: ansible.netcommon.net_put
    net_get:
      redirect: ansible.netcommon.net_get
    net_logging:
      redirect: ansible.netcommon.net_logging
    net_banner:
      redirect: ansible.netcommon.net_banner
    net_linkagg:
      redirect: ansible.netcommon.net_linkagg
    netconf:
      redirect: ansible.netcommon.netconf
    network:
      redirect: ansible.netcommon.network
    telnet:
      redirect: ansible.netcommon.telnet
    patch:
      redirect: ansible.posix.patch
    synchronize:
      redirect: ansible.posix.synchronize
    win_copy:
      redirect: ansible.windows.win_copy
    win_reboot:
      redirect: ansible.windows.win_reboot
    win_template:
      redirect: ansible.windows.win_template
    win_updates:
      redirect: ansible.windows.win_updates
    fortios_config:
      redirect: fortinet.fortios.fortios_config
    eos:
      redirect: arista.eos.eos
    asa:
      redirect: cisco.asa.asa
    ios:
      redirect: cisco.ios.ios
    iosxr:
      redirect: cisco.iosxr.iosxr
    nxos:
      redirect: cisco.nxos.nxos
    nxos_file_copy:
      redirect: cisco.nxos.nxos_file_copy
    bigip:
      redirect: f5networks.f5_modules.bigip
    bigiq:
      redirect: f5networks.f5_modules.bigiq
    junos:
      redirect: junipernetworks.junos.junos
    dellos10:
      redirect: dellemc.os10.os10
    dellos9:
      redirect: dellemc.os9.os9
    dellos6:
      redirect: dellemc.os6.os6
    vyos:
      redirect: vyos.vyos.vyos
  become:
    doas:
      redirect: community.general.doas
    dzdo:
      redirect: community.general.dzdo
    ksu:
      redirect: community.general.ksu
    machinectl:
      redirect: community.general.machinectl
    pbrun:
      redirect: community.general.pbrun
    pfexec:
      redirect: community.general.pfexec
    pmrun:
      redirect: community.general.pmrun
    sesu:
      redirect: community.general.sesu
    enable:
      redirect: ansible.netcommon.enable
  cache:
    memcached:
      redirect: community.general.memcached
    pickle:
      redirect: community.general.pickle
    redis:
      redirect: community.general.redis
    yaml:
      redirect: community.general.yaml
    mongodb:
      redirect: community.mongodb.mongodb
  callback:
    actionable:
      redirect: community.general.actionable
    cgroup_memory_recap:
      redirect: community.general.cgroup_memory_recap
    context_demo:
      redirect: community.general.context_demo
    counter_enabled:
      redirect: community.general.counter_enabled
    dense:
      redirect: community.general.dense
    full_skip:
      redirect: community.general.full_skip
    hipchat:
      redirect: community.general.hipchat
    jabber:
      redirect: community.general.jabber
    log_plays:
      redirect: community.general.log_plays
    logdna:
      redirect: community.general.logdna
    logentries:
      redirect: community.general.logentries
    logstash:
      redirect: community.general.logstash
    mail:
      redirect: community.general.mail
    nrdp:
      redirect: community.general.nrdp
    'null':
      redirect: community.general.null
    osx_say:
      redirect: community.general.osx_say
    say:
      redirect: community.general.say
    selective:
      redirect: community.general.selective
    slack:
      redirect: community.general.slack
    splunk:
      redirect: community.general.splunk
    stderr:
      redirect: community.general.stderr
    sumologic:
      redirect: community.general.sumologic
    syslog_json:
      redirect: community.general.syslog_json
    unixy:
      redirect: community.general.unixy
    yaml:
      redirect: community.general.yaml
    grafana_annotations:
      redirect: community.grafana.grafana_annotations
    aws_resource_actions:
      redirect: amazon.aws.aws_resource_actions
    cgroup_perf_recap:
      redirect: ansible.posix.cgroup_perf_recap
    debug:
      redirect: ansible.posix.debug
    json:
      redirect: ansible.posix.json
    profile_roles:
      redirect: ansible.posix.profile_roles
    profile_tasks:
      redirect: ansible.posix.profile_tasks
    skippy:
      redirect: ansible.posix.skippy
    timer:
      redirect: ansible.posix.timer
    foreman:
      redirect: theforeman.foreman.foreman
    # 'collections' integration test entries, do not remove
    formerly_core_callback:
      redirect: testns.testcoll.usercallback
    formerly_core_removed_callback:
      redirect: testns.testcoll.removedcallback
    formerly_core_missing_callback:
      redirect: bogusns.boguscoll.boguscallback
  doc_fragments:
    a10:
      redirect: community.network.a10
    aireos:
      redirect: community.network.aireos
    alicloud:
      redirect: community.general.alicloud
    aruba:
      redirect: community.network.aruba
    auth_basic:
      redirect: community.general.auth_basic
    avi:
      redirect: community.network.avi
    ce:
      redirect: community.network.ce
    cloudscale:
      redirect: cloudscale_ch.cloud.api_parameters
    cloudstack:
      redirect: ngine_io.cloudstack.cloudstack
    cnos:
      redirect: community.network.cnos
    digital_ocean:
      redirect: community.digitalocean.digital_ocean
    dimensiondata:
      redirect: community.general.dimensiondata
    dimensiondata_wait:
      redirect: community.general.dimensiondata_wait
    docker:
      redirect: community.general.docker
    emc:
      redirect: community.general.emc
    enos:
      redirect: community.network.enos
    exoscale:
      redirect: ngine_io.exoscale.exoscale
    gcp:
      redirect: google.cloud.gcp
    hetzner:
      redirect: community.general.hetzner
    hpe3par:
      redirect: community.general.hpe3par
    hwc:
      redirect: community.general.hwc
    ibm_storage:
      redirect: community.general.ibm_storage
    infinibox:
      redirect: infinidat.infinibox.infinibox
    influxdb:
      redirect: community.general.influxdb
    ingate:
      redirect: community.network.ingate
    ipa:
      redirect: community.general.ipa
    ironware:
      redirect: community.network.ironware
    keycloak:
      redirect: community.general.keycloak
    kubevirt_common_options:
      redirect: community.general.kubevirt_common_options
    kubevirt_vm_options:
      redirect: community.general.kubevirt_vm_options
    ldap:
      redirect: community.general.ldap
    lxca_common:
      redirect: community.general.lxca_common
    manageiq:
      redirect: community.general.manageiq
    mysql:
      redirect: community.mysql.mysql
    netscaler:
      redirect: community.network.netscaler
    nios:
      redirect: community.general.nios
    nso:
      redirect: community.network.nso
    oneview:
      redirect: community.general.oneview
    online:
      redirect: community.general.online
    onyx:
      redirect: mellanox.onyx.onyx
    opennebula:
      redirect: community.general.opennebula
    openswitch:
      redirect: community.general.openswitch
    oracle:
      redirect: community.general.oracle
    oracle_creatable_resource:
      redirect: community.general.oracle_creatable_resource
    oracle_display_name_option:
      redirect: community.general.oracle_display_name_option
    oracle_name_option:
      redirect: community.general.oracle_name_option
    oracle_tags:
      redirect: community.general.oracle_tags
    oracle_wait_options:
      redirect: community.general.oracle_wait_options
    ovirt_facts:
      redirect: community.general.ovirt_facts
    panos:
      redirect: community.network.panos
    postgres:
      redirect: community.general.postgres
    proxysql:
      redirect: community.proxysql.proxysql
    purestorage:
      redirect: community.general.purestorage
    rabbitmq:
      redirect: community.rabbitmq.rabbitmq
    rackspace:
      redirect: community.general.rackspace
    scaleway:
      redirect: community.general.scaleway
    sros:
      redirect: community.network.sros
    utm:
      redirect: community.general.utm
    vexata:
      redirect: community.general.vexata
    vultr:
      redirect: ngine_io.vultr.vultr
    xenserver:
      redirect: community.general.xenserver
    zabbix:
      redirect: community.zabbix.zabbix
    k8s_auth_options:
      redirect: community.kubernetes.k8s_auth_options
    k8s_name_options:
      redirect: community.kubernetes.k8s_name_options
    k8s_resource_options:
      redirect: community.kubernetes.k8s_resource_options
    k8s_scale_options:
      redirect: community.kubernetes.k8s_scale_options
    k8s_state_options:
      redirect: community.kubernetes.k8s_state_options
    acme:
      redirect: community.crypto.acme
    ecs_credential:
      redirect: community.crypto.ecs_credential
    VmwareRestModule:
      redirect: vmware.vmware_rest.VmwareRestModule
    VmwareRestModule_filters:
      redirect: vmware.vmware_rest.VmwareRestModule_filters
    VmwareRestModule_full:
      redirect: vmware.vmware_rest.VmwareRestModule_full
    VmwareRestModule_state:
      redirect: vmware.vmware_rest.VmwareRestModule_state
    vca:
      redirect: community.vmware.vca
    vmware:
      redirect: community.vmware.vmware
    vmware_rest_client:
      redirect: community.vmware.vmware_rest_client
    service_now:
      redirect: servicenow.servicenow.service_now
    aws:
      redirect: amazon.aws.aws
    aws_credentials:
      redirect: amazon.aws.aws_credentials
    aws_region:
      redirect: amazon.aws.aws_region
    ec2:
      redirect: amazon.aws.ec2
    netconf:
      redirect: ansible.netcommon.netconf
    network_agnostic:
      redirect: ansible.netcommon.network_agnostic
    fortios:
      redirect: fortinet.fortios.fortios
    netapp:
      redirect: netapp.ontap.netapp
    checkpoint_commands:
      redirect: check_point.mgmt.checkpoint_commands
    checkpoint_facts:
      redirect: check_point.mgmt.checkpoint_facts
    checkpoint_objects:
      redirect: check_point.mgmt.checkpoint_objects
    eos:
      redirect: arista.eos.eos
    aci:
      redirect: cisco.aci.aci
    asa:
      redirect: cisco.asa.asa
    intersight:
      redirect: cisco.intersight.intersight
    ios:
      redirect: cisco.ios.ios
    iosxr:
      redirect: cisco.iosxr.iosxr
    meraki:
      redirect: cisco.meraki.meraki
    mso:
      redirect: cisco.mso.modules
    nxos:
      redirect: cisco.nxos.nxos
    ucs:
      redirect: cisco.ucs.ucs
    f5:
      redirect: f5networks.f5_modules.f5
    openstack:
      redirect: openstack.cloud.openstack
    junos:
      redirect: junipernetworks.junos.junos
    tower:
      redirect: awx.awx.auth
    ovirt:
      redirect: ovirt.ovirt.ovirt
    ovirt_info:
      redirect: ovirt.ovirt.ovirt_info
    dellos10:
      redirect: dellemc.os10.os10
    dellos9:
      redirect: dellemc.os9.os9
    dellos6:
      redirect: dellemc.os6.os6
    hcloud:
      redirect: hetzner.hcloud.hcloud
    skydive:
      redirect: community.skydive.skydive
    azure:
      redirect: azure.azcollection.azure
    azure_tags:
      redirect: azure.azcollection.azure_tags
    vyos:
      redirect: vyos.vyos.vyos
  filter:
    # test entries
    formerly_core_filter:
      redirect: ansible.builtin.bool
    formerly_core_masked_filter:
      redirect: ansible.builtin.bool
    gcp_kms_encrypt:
      redirect: google.cloud.gcp_kms_encrypt
    gcp_kms_decrypt:
      redirect: google.cloud.gcp_kms_decrypt
    json_query:
      redirect: community.general.json_query
    random_mac:
      redirect: community.general.random_mac
    k8s_config_resource_name:
      redirect: community.kubernetes.k8s_config_resource_name
    cidr_merge:
      redirect: ansible.netcommon.cidr_merge
    ipaddr:
      redirect: ansible.netcommon.ipaddr
    ipmath:
      redirect: ansible.netcommon.ipmath
    ipwrap:
      redirect: ansible.netcommon.ipwrap
    ip4_hex:
      redirect: ansible.netcommon.ip4_hex
    ipv4:
      redirect: ansible.netcommon.ipv4
    ipv6:
      redirect: ansible.netcommon.ipv6
    ipsubnet:
      redirect: ansible.netcommon.ipsubnet
    next_nth_usable:
      redirect: ansible.netcommon.next_nth_usable
    network_in_network:
      redirect: ansible.netcommon.network_in_network
    network_in_usable:
      redirect: ansible.netcommon.network_in_usable
    reduce_on_network:
      redirect: ansible.netcommon.reduce_on_network
    nthhost:
      redirect: ansible.netcommon.nthhost
    previous_nth_usable:
      redirect: ansible.netcommon.previous_nth_usable
    slaac:
      redirect: ansible.netcommon.slaac
    hwaddr:
      redirect: ansible.netcommon.hwaddr
    parse_cli:
      redirect: ansible.netcommon.parse_cli
    parse_cli_textfsm:
      redirect: ansible.netcommon.parse_cli_textfsm
    parse_xml:
      redirect: ansible.netcommon.parse_xml
    type5_pw:
      redirect: ansible.netcommon.type5_pw
    hash_salt:
      redirect: ansible.netcommon.hash_salt
    comp_type5:
      redirect: ansible.netcommon.comp_type5
    vlan_parser:
      redirect: ansible.netcommon.vlan_parser
  httpapi:
    exos:
      redirect: community.network.exos
    fortianalyzer:
      redirect: community.network.fortianalyzer
    fortimanager:
      redirect: fortinet.fortimanager.fortimanager
    ftd:
      redirect: community.network.ftd
    vmware:
      redirect: community.vmware.vmware
    restconf:
      redirect: ansible.netcommon.restconf
    fortios:
      redirect: fortinet.fortios.fortios
    checkpoint:
      redirect: check_point.mgmt.checkpoint
    eos:
      redirect: arista.eos.eos
    nxos:
      redirect: cisco.nxos.nxos
    splunk:
      redirect: splunk.es.splunk
    qradar:
      redirect: ibm.qradar.qradar
  inventory:
    # test entry
    formerly_core_inventory:
      redirect: testns.content_adj.statichost
    cloudscale:
      redirect: cloudscale_ch.cloud.inventory
    docker_machine:
      redirect: community.general.docker_machine
    docker_swarm:
      redirect: community.general.docker_swarm
    gitlab_runners:
      redirect: community.general.gitlab_runners
    kubevirt:
      redirect: community.general.kubevirt
    linode:
      redirect: community.general.linode
    nmap:
      redirect: community.general.nmap
    online:
      redirect: community.general.online
    scaleway:
      redirect: community.general.scaleway
    virtualbox:
      redirect: community.general.virtualbox
    vultr:
      redirect: ngine_io.vultr.vultr
    k8s:
      redirect: community.kubernetes.k8s
    openshift:
      redirect: community.kubernetes.openshift
    vmware_vm_inventory:
      redirect: community.vmware.vmware_vm_inventory
    aws_ec2:
      redirect: amazon.aws.aws_ec2
    aws_rds:
      redirect: amazon.aws.aws_rds
    foreman:
      redirect: theforeman.foreman.foreman
    netbox:
      redirect: netbox.netbox.nb_inventory
    openstack:
      redirect: openstack.cloud.openstack
    tower:
      redirect: awx.awx.tower
    hcloud:
      redirect: hetzner.hcloud.hcloud
    gcp_compute:
      redirect: google.cloud.gcp_compute
    azure_rm:
      redirect: azure.azcollection.azure_rm
  lookup:
    # test entry
    formerly_core_lookup:
      redirect: testns.testcoll.mylookup
    avi:
      redirect: community.network.avi
    cartesian:
      redirect: community.general.cartesian
    chef_databag:
      redirect: community.general.chef_databag
    conjur_variable:
      redirect: cyberark.conjur.conjur_variable
    consul_kv:
      redirect: community.general.consul_kv
    credstash:
      redirect: community.general.credstash
    cyberarkpassword:
      redirect: community.general.cyberarkpassword
    dig:
      redirect: community.general.dig
    dnstxt:
      redirect: community.general.dnstxt
    etcd:
      redirect: community.general.etcd
    filetree:
      redirect: community.general.filetree
    flattened:
      redirect: community.general.flattened
    gcp_storage_file:
      redirect: community.general.gcp_storage_file
    hashi_vault:
      redirect: community.general.hashi_vault
    hiera:
      redirect: community.general.hiera
    keyring:
      redirect: community.general.keyring
    lastpass:
      redirect: community.general.lastpass
    lmdb_kv:
      redirect: community.general.lmdb_kv
    manifold:
      redirect: community.general.manifold
    nios:
      redirect: community.general.nios
    nios_next_ip:
      redirect: community.general.nios_next_ip
    nios_next_network:
      redirect: community.general.nios_next_network
    onepassword:
      redirect: community.general.onepassword
    onepassword_raw:
      redirect: community.general.onepassword_raw
    passwordstore:
      redirect: community.general.passwordstore
    rabbitmq:
      redirect: community.rabbitmq.rabbitmq
    redis:
      redirect: community.general.redis
    shelvefile:
      redirect: community.general.shelvefile
    grafana_dashboard:
      redirect: community.grafana.grafana_dashboard
    openshift:
      redirect: community.kubernetes.openshift
    k8s:
      redirect: community.kubernetes.k8s
    mongodb:
      redirect: community.mongodb.mongodb
    laps_password:
      redirect: community.windows.laps_password
    aws_account_attribute:
      redirect: amazon.aws.aws_account_attribute
    aws_secret:
      redirect: amazon.aws.aws_secret
    aws_service_ip_ranges:
      redirect: amazon.aws.aws_service_ip_ranges
    aws_ssm:
      redirect: amazon.aws.aws_ssm
    skydive:
      redirect: community.skydive.skydive
    cpm_metering:
      redirect: wti.remote.cpm_metering
    cpm_status:
      redirect: wti.remote.cpm_status
  netconf:
    ce:
      redirect: community.network.ce
    sros:
      redirect: community.network.sros
    default:
      redirect: ansible.netcommon.default
    iosxr:
      redirect: cisco.iosxr.iosxr
    junos:
      redirect: junipernetworks.junos.junos
  shell:
    # test entry
    formerly_core_powershell:
      redirect: ansible.builtin.powershell
    csh:
      redirect: ansible.posix.csh
    fish:
      redirect: ansible.posix.fish
  test:
    # test entries
    formerly_core_test:
      redirect: ansible.builtin.search
    formerly_core_masked_test:
      redirect: ansible.builtin.search
import_redirection:
  # test entry
  ansible.module_utils.formerly_core:
    redirect: ansible_collections.testns.testcoll.plugins.module_utils.base
  ansible.module_utils.known_hosts:
    redirect: ansible_collections.community.general.plugins.module_utils.known_hosts
  # ansible.builtin synthetic collection redirection hackery
  ansible_collections.ansible.builtin.plugins.modules:
    redirect: ansible.modules
  ansible_collections.ansible.builtin.plugins.module_utils:
    redirect: ansible.module_utils
  ansible_collections.ansible.builtin.plugins:
    redirect: ansible.plugins"""
