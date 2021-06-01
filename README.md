provision_kubernetes_on_aws
=========

Provision kubernetes cluster on AWS public cloud using AWS EC2 service. Furthermore retrieve the public IPs of the instances launched creating a dynamic inventory to further configure the instances with kubernetes.

Requirements
------------

The pre-requisites for this role include installing Boto3 library. However it is not compulsary as the role will itself download the library if not present.

Role Variables
--------------
To use thie role you need to use 2 variables:
1. numberOfMasters
2. numberOfSlaves
Also you need to creat an ansible vault variable file which will consist of variables:
1. access_key : attach the AWS Access Key here
2. secret_key : attach the AWS Secret Access key here

Dependencies
------------

This role consists of 2 files masterEC2.py and slaveEC2.py. Copy these 2 files (located at files directory) to the playbook directory. These 2 files are responsible for dynamic inventory. To use these 2 files you need to export environmental variables in your shell. The environmental variables include:
1. AWS_ACCESS_KEY_ID : your AWS Access key
2. AWS_SECRET_ACCESS_KEY : your AWS Secret Access key
3. AWS_DEFAULT_REGION : default region to work with on AWS
4. NUMBER_OF_MASTERS : number of master nodes you want ( must be the same as numberOfMasters role variable)
5. NUMBER_OF_SLAVES : number of slave nodes you want ( must be the same as numberOfSlaves role variable)

Example Playbook
----------------
<pre><code>
  - name: "Provision Kubernetes cluster on AWS"
    hosts: localhost
    vars_files:
    - secret.yml
    vars_prompt:
    - name: "numberOfMaster"
      prompt: "Enter the number of Master you want"
      private: no
    - name: "numberOfSlaves"
      prompt: "Enter the number of Slaves you want"
      private: no
    roles:
    - provision_kubernetes_on_aws
    </code></pre>

Author Information
------------------

For further information you can contact me @ abhijeetkarmakar23@gmail.com
