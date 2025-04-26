{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python312.withPackages (ps: with ps; [
    numpy
    sympy
    mpmath
  ]);
in

pkgs.mkShell {
  buildInputs = [
    pythonEnv
    pkgs.zsh
  ];

  shellHook = ''
    zsh -l
  '';
}
