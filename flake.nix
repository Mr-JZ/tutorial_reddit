{
  description = "Development environment for Tutorial Reddit project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.bash
            pkgs.openssl
          ];

          shellHook = ''
            echo "Environment ready!"
            echo "Run ./setup.sh to generate configuration files"
          '';
        };
      }
    );
}
