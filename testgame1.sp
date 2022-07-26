/ Definiowanie poprawnej liczby
$liczba_poprawna = [<<ri>>x1x7]
/ Informacja dla uzytkownika
-flush Masz 1 zycie. Zgadnij liczbe (od 1 do 7)!
/Pyta uzytkownika o liczbe
-flush Wpisz swoj glos tutaj:
$odp = <<ask>>
?if $odp == $liczba_poprawna {
-flush ZGADLES!
}
?if $odp != $liczba_poprawna {
-flush NIE ZGADLES! Poprawna liczba to $liczba_poprawna!
}