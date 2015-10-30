
# Wiki Pszczelarstwa Naturalnego

Ta strona jest poświęcona ogólnie rozumianemu pszczelarstwu ze szczególnym naciskiem na zagadnienia pszczelarstwa naturalnego. Przyświeca jej idea promowana przez stowarzyszenie [Wolne Pszczoły](http://wolnepszczoly.org) zdrowych i szczęśliwych pszczół bez trucia ich niepotrzebną chemią, która na dzień dzisiejszy stała się przykrą rzeczywistością większości pasiek. Ma to szeroko pojęte negatywne skutki tak dla samych rodzin pszczelich jak i konsumentów końcowych produktów pszczelich.

Zapraszamy do lektury [Wiki](https://github.com/wolnepszczoly/wikipn/wiki)


## Informacje na temat budowania wiki

Końcowa Wiki jest budowana statycznie z github wiki (projekt [gollum](https://github.com/gollum/gollum/wiki)) poprzez nasz własny mechanizm przy użyciu pythonowego skryptu i [MkDocs](http://www.mkdocs.org/).

```
pip install -r requirements.txt
python convert.py
mkdocs build
```
