# ansible-aci

This repository contains example Ansible Playbooks to Configure Cisco ACI

## Install Ansible

```bash
sudo pip install ansible
```

## Install Galaxy Collections: ND, MSO

```bash
ansible-galaxy collection install cisco.aci
```

## Run the Playbook

```bash
cd aaep-to-epg
ansible-playbook -i production playbook.yaml
```