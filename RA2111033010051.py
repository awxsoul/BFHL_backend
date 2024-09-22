from flask import Flask, request

RA2111033010051 = Flask(__name__)

#server data has the info of user id, colllge email and college rollnumber 
server_data=["gopikrishna_17042003","gd0002@srmist.edu.in","RA2111033010051"]

@RA2111033010051.route('/bfhl', methods=['GET', 'POST'])
def data_response():
    if request.method == 'GET':
        data = {
            'is_success': True,
            'user_id': server_data[0],
            'college_email':server_data[1],
            'college_rollnumber':server_data[2],
            'status': 'success'}
        return data, 200 

    if request.method == 'POST':
        req= request.get_json()
        a=[] #alphabets in the data
        n=[] #number in the data
        ha=["Z"] #highest before lower letters

        for i in req["data"]: #organising num and alpha to respective lists
            if i.isalpha():
                a.append(i)
            elif i.isnumeric():
                n.append(i)
        for i in a: #checking the highest lowercase in alpha list
            if i>ha[0]:
                ha[0]=i
        if ha[0]=="Z": #if no lowercase alpha is found
            ha.pop()

        #filehandling
        if 'file_bs64' in req.keys():
            fv=True
        else:
            fv=False
        #formatting
        data={
            'is_success': True,
            'user_id': server_data[0],
            'college_email':server_data[1],
            'college_rollnumber':server_data[2],
            'numbers':n,
            'alphabets':a,
            'highest_lowercase_alphabet':ha,
            'file_valid':fv
        }
        
        return data, 201
              

if __name__ == '__main__':
    RA2111033010051.run(debug=True)
