'''
#Program that run till the balance becomes '0'

vehicle = {'car': 70, 'Lorry': 150, 'Bus': 100, 'Two-wheeler': 0}
balance = 1000
pending_balance = 0

while pending_balance<=balance:
    user_input = input('Enter your vehicle details ')
    
    if user_input == 'Two-wheeler':
        print(f'Thank you for your visit !')

    else:
        if balance >= vehicle[user_input]: 
            balance -= vehicle[user_input]
            print("You have successfully paid the amount")
            print(f'Your balance is {balance}')
        else:
            print('Insufficient balance. Please top up your fast track balance')

    if balance == pending_balance:
        break


#Program that will save 2 driver details and validate

vehicle = {'car': 70, 'Lorry': 150, 'Bus': 100, 'Two-wheeler': 0}
driver_details = {'Driver1': 'ABC123', 'Driver2': 'ABC001'}
balance = 1000
pending_balance = 0

while pending_balance <= balance:

    driver_input = input('Enter your driver details: ')
    if driver_input in driver_details.values():
        vehicle_input = input('Enter your vehicle type: ')
    
        if vehicle_input == 'Two-wheeler':
            print('Thank you for your visit!')
        else:
            if vehicle_input in vehicle:        
                if balance >= vehicle[vehicle_input]: 
                    balance -= vehicle[vehicle_input]
                    print("You have successfully paid the amount.")
                    print(f'Your balance is {balance}.')
                else:
                    print('Insufficient balance. Please top up your fast track balance.')
            else:
                print('Invalid vehicle type.')
                break
    else:
        print('Invalid driver details.')
        break

#Program that maintain the balance amount individually

vehicle = {'car': 70, 'Lorry': 150, 'Bus': 100, 'Two-wheeler': 0}
driver_details = {'Driver1':{'License': 'ABC123', 'Balance': 1000},
                  'Driver2':{'License': 'AAA123', 'Balance': 1000}
                  }
while True:
    driver_input = input('Enter your driver details: ')

    if driver_input in driver_details:
        driver = driver_details[driver_input] # {'Driver1':{'License': 'ABC123', 'Balance': 1000}
        license_input = input('Enter your License details: ')

        if license_input == driver['License']: # ABC123
            vehicle_type = input('Enter your vehicle type: ')

            if vehicle_type in vehicle: #Train
                amount = vehicle[vehicle_type] #70

                if amount > driver['Balance']: #70 > 1000
                    print('Insufficient Balance. Please top up')

                else:
                    driver["Balance"] -= amount #driver['Balance'] = driver['Balance'] - amount #1000-70 = 930
                    print('Thank you for your visit')
                    print(f'Your balance Fast-Track amount is {driver["Balance"]}')

            else:
                print('Invalid vehicle type')
                break
        else:
            print('Invalid License details')
            break

    if driver["Balance"] == 0:
        print ('Your account has been suspended due to insufficient funds')
        break
'''

Driver = {'Driver1':{'License':'ABC123', 'Balance':1000},
          'Driver2':{'License':'AAA123','Balance':1000}}

Vehicle = {'car':70, 'Bus':100, 'Lorry': 150, 'Two-wheeler':0}

while True:
    DriverName=input("Please enter a name of the driver: ")

    if DriverName in Driver:
        driver_details = Driver[DriverName]
        Driving_license = input("Please enter your License Details ")

        if Driving_license == driver_details['License']:
            VehicleType=input("Please Enter Your Vehicle Type ")

            if VehicleType not in Vehicle:
                print ("Sorry! We don't have any records")

            elif Vehicle[VehicleType]>driver_details['Balance']:
                print('Insufficient Balance')
            else:
                Amount = int(Vehicle[VehicleType])
                driver_details['Balance']-=Amount
                print('Thank you for your Visit')
                print(f'Your Balance Fast-Track is {driver_details["Balance"]}')
        else:
            print('Incorrect License Number')
    else:
        print ('Incorrect Driver details')





