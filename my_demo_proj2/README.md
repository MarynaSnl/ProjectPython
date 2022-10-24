# Demo description

<hr>
  Napisz aplikacje która będzie wspomagała zespół inżynierów i naukowców w ich zadaniach.
Aplikacja ma składać sie z kilku funkcjonalności.

+ Musi posiadać menu, w którym na początku działania programu użytkownik może wybrać czy jest naukowcem, czy inżynierem.
+ Dla każdej z profesji będzie osobny zestaw funkcji
	- naukowcy:
		- oblicz BMI - wg klasycznego wzoru na BMI - wartości zmienne mają być wprowadzane przez użytkownika
		- oblicz procent z danej liczby lub liczbę z danego procenta. Funckja ma dwa tryby działania. W pierwszej podajemy jakąś liczbę i sprawdzamy jakim procentem tej liczby jest inna liczba (podana jako drugi parametr- np. 100, 10 =  10%). W drugim przykładzie podajemy liczbę i procent i obliczamy jaką liczbą jest ten procent (100, 10%, wynik to liczba 10.)
		- oblicz stężenie molowe roztworu. Użytkownik podaje dwie wartości - liczbę moli i objętość roztworu. Stężenie molowe to dzielnie moli przez objętość zgodnie ze wzorem - https://www.swiatchemii.pl/chemia-ogolna/stezenie-molowe-omowienie#:~:text=St%C4%99%C5%BCenie%20molowe%20wyra%C5%BCa%20si%C4%99%20jako,substancji%20rozpuszczonej%20do%20obj%C4%99to%C5%9Bci%20roztworu.&text=St%C4%99%C5%BCenie%20molowe%20jest%20to%20ilo%C5%9B%C4%87,%5Bmol%2Fdm3%5D.
	
	- Inżynierowie:
		- oblicz pole i obwód okręgu - użytkownik podaje tylko promień zgodnie ze wzroem
		- wypisz ciąg fibbonacciego do n elemetnu. https://matematyka.poznan.pl/artykul/ciag-fibonacciego-jako-test-pierwszosci/#:~:text=M%C3%B3wi%C4%85c%20%C5%9Bci%C5%9Blej%2C%20ci%C4%85g%20Fibonacciego%20jest,a2bn2.
		czyli np fibbonacci(4) wypisze nam 0,1,1,2,3 - bo czwórki już w fibbonacim nie ma, a 5 jest za dużą wartością.


Poziom zaawansowany zadania powyżej:

	- do każdej funckji stwórz plik wynik_nazwa_funkcji.txt, gdzie będą zapisywane wszystkie wyniki, jeden pod drugim. Czyli np. funkcja oblicz_BMI będzie miała plik BMI.txt gdzie będą trafiały wyniki działań
	- dopisz do funkcji oblicz pole i obwód okręgu funkcjonalnosć która umożliwi importowanie i obliczanie wielu promieni z pliku csv.


Poziom maksymalny:
	- zmodyfikuj pierwszy punkt z zadania zaawansowanego tak by w plikach zapisywały sie nie tylko wyniki ale wartości wejściowe. Czyli ktoś oblicza pole koła i wpisuje promień 4, to w pliku powinna się znaleźc linijka "4,wynik"


<hr>


[Proj_2.py](https://github.com/MarynaSnl/my_demo_proj/tree/main/my_demo_proj2/Proj_2.py) - Solution.

[test2.py](https://github.com/MarynaSnl/my_demo_proj/tree/main/my_demo_proj2/test2.py) - tests for  Proj_2.py (Unittest


<hr>

