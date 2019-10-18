#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    t = 11,22,33,44,55,66,77
    users = ['anna','markus','john','maria']
    mails = ['anna@no.com','markus@no.com','john@no.com','maria@no.com']

    for data in zip(t,users,mails):
        idx, name, mail  = data
        print(f'idx={idx}, name={name}, mail={mail}, data = {data}')