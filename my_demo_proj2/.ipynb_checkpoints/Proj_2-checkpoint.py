import math
import pandas as pd
import os as os

class Pracownik:
    def __init__(self, nazwa):
        self.nazwa = nazwa 
         
    def informacje(self):
        print(f" Obliczenia wykonywane przez specjalistę {self.nazwa}")
        return
        
class Naukowec(Pracownik):
    def __init__(self, nazwa):
        super().__init__(nazwa)

    def oblicz_BMI(self):
        # massa/(rost*rtost)
        try:
            massa = int(input("Wprowadź masę ciała:"))
        except:
            print(f" Nieprawidłowe dane, musisz wpisać liczbę. ")    
            return False
        try:
            wysokosc = int(input("Wpisz wysokość  (w sm) :"))
            if wysokosc == 0:
                print(f" Nieprawidłowe dane, wysokość nie może być 0. ") 
                return False
        except:
            print(f" Nieprawidłowe dane, musisz wpisać liczbę. ")    
            return False
        BMI = round(massa/(wysokosc/100 *wysokosc/100),2)
        ss = f"Massa={massa},wzrost={wysokosc}sm,BMI={BMI}"
        dobaj_do_pliku(ss, "oblicz_BMI.txt")
        #print(f" Massa = {massa}, wysokość = {wysokosc}, BMI = {BMI} ")
        print(ss)
        return BMI
        
    def oblicz_procent_liczbu(self, liczba1, liczba2, numer_obliczenia = 1):   
        #podajemy jakąś liczbę i sprawdzamy jakim procentem tej liczby jest inna liczba (podana jako drugi parametr-
        #np. 100, 10 =  10%). W drugim przykładzie podajemy liczbę i procent i obliczamy jaką liczbą jest ten procent 
        #(100, 10%, wynik to liczba 10.) 
        
        if numer_obliczenia == 2:
            if liczba1 == 0:
                print(f" Nieprawidłowe dane, pierwsza liczba nie może być 0. ")
                return False
            else:
                proc_liczba = liczba2*100/liczba1
                ss = f"{liczba2} to jest {proc_liczba}% od {liczba1}"
                #print(f" {liczba2} to jest {proc_liczba}% od {liczba1}")
                print(ss)
                dobaj_do_pliku(ss, "oblicz_procent_liczbu.txt")
                return proc_liczba
        else:
            proc_liczba = liczba1/100 * liczba2
            #print(f"Od  {liczba1} {liczba2}%  to liczba {proc_liczba}")
            ss = f"Od {liczba1} {liczba2}% to liczba {proc_liczba}"
            dobaj_do_pliku(ss, "oblicz_procent_liczbu.txt")
            return proc_liczba
        
    def oblicz_stezenie_molowe_roztworu(self, liczbe_moli, objetosc_roztworu):   
        # Cm=nVr  Cm - stężenie molowe [mol/dm3]  n - liczba moli [mol]  Vr - objętość roztworu [dm3]
        if objetosc_roztworu == 0:
            print(f" Nieprawidłowe dane, nieustawiona 'objetosc roztworu'. ")
            return False
        else:
            stezenie_molowe = liczbe_moli/objetosc_roztworu
            ss=f"Stezenie molowe:{stezenie_molowe}"
            print(ss)
            dobaj_do_pliku(ss, "oblicz_stezenie_molowe_roztworu.txt")
            return stezenie_molowe
                
class Inżynier(Pracownik): 
    def __init__(self, nazwa):
        super().__init__(nazwa)
        
    def oblicz_pole_i_obwod_okregu(self, promien, dodac_do_pliku=True):
        # oblicz pole i obwód okręgu
        pole  = 2 * math.pi * promien 
        obwod = math.pi * promien * promien
        ss = f"Promien:{promien},wynik-Pole:{round(pole,5)},Obwod:{round(obwod,5)}"
        if dodac_do_pliku == True:
            dobaj_do_pliku(ss, "oblicz_pole_i_obwod_okregu.txt")  
        return ss
        #eturn pole, obwod
        
    def wypisz_ciag_fibbonacciego(self, n):   
        # wypisz ciąg fibbonacciego do n elemetnu
        # Fn+2=Fn+1+Fn,
        # F1=F2=1   f0 = 0,  f1 = 1 , Fn = Fn-1  + Fn-2 
        x = []
        for i in range(n+1): 
            if i == 0:
                x.append(0)
            elif i == 1:
                x.append(1)
            else:
                x.append(x[i-1] + x[i-2])
        ss = "ciag fibbonacciego od "+str(n)+"-"
        dobaj_do_pliku(x, "wypisz_ciag_fibbonacciego.txt", ss)
        print(x)
        return x
    
def stworz_test_df():
    data = {"promien": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2,22,11,1,34,12]} 
    df = pd.DataFrame(data)
    #df.to_csv(nazwa_pliku)    
    return df   


def wczytaj_dane(nazwa_pliku):
    try:
        df = pd.read_csv(nazwa_pliku, header=None, sep=",")
    except:
        print(f"Nie znaleziono pliku: {nazwa_pliku}")
        df = stworz_test_df()
    return df

#def open_txt_file(f_path):
#    with open(f_path, 'a') as file_for_zapis:
#        return file_for_zapis
    
def dobaj_do_pliku(df_str, f_path, *args ):
    #print(type(df_str))
    with open(os.path.join(os.getcwd(), f_path),'a') as outfile:
        if len(args) > 0:
            for arg in args:
                outfile.write(str(arg))
        if (isinstance(df_str, str)):
            outfile.write(df_str)
        elif (isinstance(df_str, (list,set,tuple))):
            for x in df_str:
                outfile.write(str(x)+',')
        elif (isinstance(df_str, (int,float ))):    
            outfile.write(str(x)+',')  
        elif isinstance(df_str, pd.DataFrame):    
            outfile.write("\n")
            df.to_string(outfile)

            
print("1 - naukowec\n2 - inżynier.\n")
pracownik = 0
for i in range(3):
    try:
        pracownik = int(input("Wprowadź  1  lub  2."))
        if pracownik > 2 or pracownik < 0:
            print(f" Nieprawidłowe dane, musisz wpisać 1 lub 2. ")
            pracownik = 0
        else:
            break
    except:
        print(f" Nieprawidłowe dane, musisz wpisać liczbę. ")

if pracownik != 0:
    if pracownik == 1:
        new_pracownik = Naukowec("Jan Nowak")
        new_pracownik.informacje()
        ss = new_pracownik.oblicz_procent_liczbu(100, 12, 1)
            
        new_pracownik.oblicz_BMI()
        new_pracownik.oblicz_procent_liczbu(100, 12, 2)
        new_pracownik.oblicz_stezenie_molowe_roztworu(120, 35)
    else:
        new_pracownik = Inżynier("Olek Komiński")
        new_pracownik.informacje()
        new_pracownik.oblicz_pole_i_obwod_okregu(12, True)
        new_pracownik.wypisz_ciag_fibbonacciego(0)
        new_pracownik.wypisz_ciag_fibbonacciego(1)
        new_pracownik.wypisz_ciag_fibbonacciego(2)
        new_pracownik.wypisz_ciag_fibbonacciego(3)
        new_pracownik.wypisz_ciag_fibbonacciego(4)
        new_pracownik.wypisz_ciag_fibbonacciego(5)
        new_pracownik.wypisz_ciag_fibbonacciego(10)
        
        df = wczytaj_dane("test_file.csv")
        
        dobaj_do_pliku(df["promien"].apply(new_pracownik.oblicz_pole_i_obwod_okregu) , "oblicz_procent_liczbu.txt")       
    