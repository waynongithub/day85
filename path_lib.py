from pathlib import Path

file = "/media/datax/coding/images/sigmasian-012.png"
filename = "sigmasian-012.png"
print(f"current working dir: Path(): {Path()}")
print(f"current working dir: Path().resolve(): {Path().resolve()}")
print(f"current working dir: Path.cwd(): {Path.cwd()}")
print(f"turn a string into a Path object: Path(file): {type(Path(file))}")
print(f"Path(filename): {Path(filename)}, type={type(Path(filename))}")
f = Path(filename)
print(f"f: {f}, type={type(f)}")
print(f"f.resolve(): {f.resolve()}, type={type(f.resolve())}")
# print(f"Path(filename).resolve()")
print(f"f.resolve().exists() : {f.resolve().exists()}")
print(f"Path('main.py').exists() : {Path('main.py').exists()}")
print(f"Path('main.py').resolve().exists() : {Path('main.py').resolve().exists()}")
print(f"Path('main.py').resolve().is_dir() : {Path('main.py').resolve().is_dir()}")
print(f"Path('main.py').resolve().is_file() : {Path('main.py').resolve().is_file()}")
print(f"Path('main.py').resolve().is_symlink() : {Path('main.py').resolve().is_symlink()}")

print(f"Path(file).name : {Path(file).name}")
print(f"Path(file).stem : {Path(file).stem}")
print(f"Path(file).parent : {Path(file).parent}")
print(f"Path(file).suffix : {Path(file).suffix}")
print(f"Path(file).parts : {Path(file).parts}")

# print(f"create path with different extension: Path(file).parent / Path(file).stem / '.txt' : {Path(file).parent / Path(file).stem / '.txt'}")
print(f"joinpath: {print(Path(file).joinpath(Path(file)).with_suffix('.watermarked').with_suffix('.txt'))}")

# TODO : create new file
# TODO : create new file with suffix
# TODO : create new file with different extension
# TODO :

print("--------------")

# creating a dir that already exists still throws a FileExistError, but it is ignored => no crash
# print(f"make dir: Path(‘example_dir’).mkdir() {Path('example_dir').mkdir()}")
# print(f"make dir: Path(‘example_dir’).mkdir() {Path('example_dir').mkdir()}")

# Listing subdirectories:
print("print the fucking subdirs")
p = Path('.')
subdirs = [x for x in p.iterdir() if x.is_dir()]
for s in subdirs:
    print(f"p={p}, subdir={s}, subdir.resolve={s.resolve()}")

# Listing Python source files in this directory tree: oh fuck, this is recursive
print(list(p.glob('**/*.py')))

# Navigating inside a directory tree:
p = Path('/etc')
q = p / 'init.d' / 'reboot'
print(q.resolve())