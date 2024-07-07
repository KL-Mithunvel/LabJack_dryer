def csv_write(env):
    f=input('Enter the File name:')
    tl = env['tl']
    file_obj = open(f, 'w', newline='')
    write_obj=csv.writer(file_obj)
    write_obj.writerow(['f_target_temp','f_achieved_temp','fuel_added'])
    for i in range(len(tl)):
        write_obj.writerow([tl[i]['f_target_temp'],tl[i]['f_achieved_temp'],tl[i]['fuel_added']])




def export_data(env, f):
    tl = env['tl']
    file_obj = open(f, 'w')
    file_obj.write(str(['f_target_temp','f_achieved_temp','fuel_added']))
    for i in range(len(tl)):
        file_obj.write(str([tl[i]['f_target_temp'], tl[i]['f_achieved_temp'], tl[i]['fuel_added']]))
    pass
