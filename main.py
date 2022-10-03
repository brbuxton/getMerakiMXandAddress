#!/usr/bin/env python3

import meraki
import csv

API_KEY = ""
dashboard = meraki.DashboardAPI(API_KEY)
organizations = dashboard.organizations.getOrganizations()


def merakitocsv(dashboard):
    print(organizations)
    print(dashboard.organizations.getOrganizationDevices(organizations[0]['id']))
    device_list: list
    device_list = [serial for serial in dashboard.organizations.getOrganizationDevices(organizations[0]['id'])
                   if serial['productType'] == 'appliance']
    print(device_list)
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'serial', 'model', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in device_list:
            writer.writerow({'name': row['name'], 'serial': row['serial'], 'model': row['model'],
                             'address':row['address']})




if __name__ == '__main__':
    merakitocsv(dashboard)

