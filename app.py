from flask import Flask, request, render_template
from Bio.Seq import Seq
import re

app = Flask(__name__)


@app.route('/')
def determine_seq_type():

    dna_nucl = re.search(r'[^AGTCN]', seq.upper())
    if dna_nucl:
        rna_nucl = re.search(r'[^AGUCN]', seq.upper())
        if rna_nucl:
            prot = re.search(r'[^ACDEFGHIKLMNPQRSTVWY]', seq.upper())
            if prot:
                return render_template('W4.html', protein="")


if __name__ == '__main__':
    app.run(debug=True)
