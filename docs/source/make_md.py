import pypandoc
import glob

def make_md_table(filenames, outfile):
    with open(outfile, "w") as f:
        f.write("| Circuit | Hamiltonian |\n")
        f.write("| ------- | ----------- |\n")
        for fn in filenames:
            f.write(f"|![]({fn})|placeholder|\n")


if __name__ == "__main__":
    filenames = glob.glob("img/3_node_circuits/*")
    make_md_table(filenames, "3_node_circuits.md")
    output = pypandoc.convert_file("3_node_circuits.md", "rst")
    with open("api.rst", "w") as f:
        f.write(output)
    