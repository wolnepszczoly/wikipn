Ó
# Wiki Pszczelarstwa Naturalnego

Ta strona jest poświęcona ogólnie rozumianemu pszczelarstwu ze szczególnym naciskiem na zagadnienia pszczelarstwa naturalnego. Przyświeca jej idea promowana przez stowarzyszenie [Wolne Pszczoły](http://wolnepszczoly.org) zdrowych i szczęśliwych pszczół bez trucia ich niepotrzebną chemią, która na dzień dzisiejszy stała się przykrą rzeczywistością większości pasiek. Ma to szeroko pojęte negatywne skutki tak dla samych rodzin pszczelich jak i konsumentów końcowych produktów pszczelich.

Zapraszamy do lektury [Wiki](http://wolnepszczoly.github.io) lub edycji [Wiki](https://github.com/wolnepszczoly/wikipn/wiki)

## Jak współtworzyć wiki

Wiki jest tworzona przez Stowarzyszenie [Pszczelarstwa Naturalnego "Wolne Pszczoły"](http://wolnepszczoly.org), jeśli jesteś jego członkiem bądź tak czy inaczej bardzo chcesz współtworzyć wiki, stwórz konto na [Githubie](https://github.com), a następnie poproś o dostęp do niego na forum Wolnych Pszczół podając swoją nazwę użytkownika.

Wiki jest pisana w [Markdown](https://pl.wikipedia.org/wiki/Markdown), jest to metoda opisywania tekstu specjalnymi znacznikami, które następnie są zamieniane na porządaną formę. Github Wiki ma dodatkowo edytor z podglądem i pomocą (ikona znaku zapytania w edytorze), co dodatkowo ułatwia edycję.

## Informacje na temat budowania wiki

Końcowa Wiki jest budowana statycznie z github wiki (projekt [gollum](https://github.com/gollum/gollum/wiki)) poprzez nasz własny mechanizm przy użyciu pythonowego skryptu i [MkDocs](http://www.mkdocs.org/).

### Instalowanie
Można użyć virtualenv, jeśli nie to po prostu:
```bash
pip install -r requirements.txt
```
### Budowanie
Są dwa skrypty jeden wstępnie przetwarzający źródła `convert.py` i drugi który odrazu wysyła strone na server `deploy.py`, standardowo będąc w katalogu projektu wykonujemy:
```bash
python deploy.py
```

