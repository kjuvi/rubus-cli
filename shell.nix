{ nixpkgs ? import <nixpkgs> {} }:

# src: https://github.com/NixOS/nixpkgs/issues/71178#issuecomment-562609408

with nixpkgs;

stdenv.mkDerivation rec {

  name = "python-virtualenv-shell";

  env = buildEnv { name = name; paths = buildInputs; };

  buildInputs = [
    python3
    python3Packages.virtualenv
    python3Packages.flake8
    python3Packages.python-language-server
    # It is essential **not** to add `pip` here as
    # it would prevent proper virtualenv creation.
  ];

  shellHook = ''
    # set SOURCE_DATE_EPOCH so that we can use python wheels
    SOURCE_DATE_EPOCH=$(date +%s)
    if [ ! -d venv/ ]; then
     virtualenv venv
    fi
    source venv/bin/activate
  '';
}
