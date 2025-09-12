import os
import sys

if __name__ == "__main__":

    # Get the service name from the first command line argument
    service_name = sys.argv[1]

    # Check if the service is active using systemctl; returns 0 if running
    status = os.system(f'systemctl is-active --quiet {service_name}')
    
    if status == 0:
        # If the service is running, print its status
        print(f"The service '{service_name}' is running.")
        print(os.system(f'systemctl status {service_name} --no-pager'))
    else:
        # If the service is not running, prompt the user to start it
        start_service = input("Do you want to start the service? y/n: ")
        if start_service.lower() == 'y':
            os.system(f'sudo systemctl start {service_name}')
            print(f"The service '{service_name}' has been started.")
            print(os.system(f'systemctl status {service_name}'))