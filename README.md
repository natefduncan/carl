# Carl

Carl is a tool that runs Monte Carlo simulations on deterministic spreadsheet models for sensitivity analysis. The spreadsheet engine currently uses [LibreOffice](https://www.libreoffice.org/), but I would love to add more options or switch to something cleaner in the future. 

## Installation

- Install [LibreOffice](https://www.libreoffice.org/)
- Clone and install this repo
- Ensure that your Python environment has the `uno.py` and `unohelper.py` in it's `PATH`

## Example

- Run example simulation: `carl simulate -c ./examples/example.toml ./examples/example.ods -n 1000`
- Run example simluation with visualization (I know this is ugly): `carl simulate -c ./examples/example.toml ./examples/example.ods -n 1000 | jq -r '.[].outputs."Output 1"[0][0]' | awk 'BEGIN {print "Output 1"} {print $0}' | p9 plot -f - 'ggplot(df, aes(x="Output 1")) + geom_histogram()' | timg -` 

![image](https://github.com/user-attachments/assets/6dab9db5-c0d1-4612-9f39-9cb72e23f94f)
