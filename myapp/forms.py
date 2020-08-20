from django import forms
choice_date=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')]
choice_month=[('1','Jan'),('2','Feb'),('3','Mar'),('4','Apr'),('5','May'),('6','Jun'),('7','Jul'),('8','Aug'),('9','Sept'),('10','Oct'),('11','Nov'),('12','Dec')]
choice_year=[('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')] 
class SampleForm(forms.Form):
    first_name=forms.CharField(max_length=20, required=True,help_text='No space and special character is allowed')
    last_name=forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'placeholder':'last name'}))
    email= forms.EmailField(max_length=30, required=True)
    phno=forms.IntegerField(max_value=9999999999,min_value=6000000000, required=True,help_text='No country code')
    pwd= forms.CharField(max_length=20,required=True,label="Password",widget=forms.PasswordInput)
    birthday=forms.ChoiceField(choices=choice_date, required=True,label='Birthday')
    birthmonth=forms.ChoiceField(choices=choice_month, required=True,label='Birthmonth')
    birthyear=forms.ChoiceField(choices=choice_year, required=True,label='Birthyear')
    gender= forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], required=True,widget=forms.RadioSelect)
    languages=forms.MultipleChoiceField(choices=[('python','python'),('java','java'),('C#','C#')], required=True)
    language= forms.MultipleChoiceField(choices=[('python','python'),('java','java'),('C#','C#')], required=True, widget=forms.CheckboxSelectMultiple)
    image= forms.ImageField(required=True,label='Profile Pic')