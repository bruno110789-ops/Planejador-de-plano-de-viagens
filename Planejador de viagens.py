distance_mi = 6      #distância em milhas
is_raining = False    #se está chovendo
has_bike = True      #se possui bicicleta
has_car = True       #se possui carro
has_ride_share_app = True     #se possui aplicativo de corrida

if distance_mi == 0:
    print('False')
elif distance_mi <= 1 and not is_raining:
    print('True')
elif (distance_mi > 1 and distance_mi <= 6) and has_bike and not is_raining:
    print('True')
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')
else:
    print('False')