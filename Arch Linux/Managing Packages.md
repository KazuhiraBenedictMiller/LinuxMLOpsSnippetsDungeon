mportant Notes:

sudo: Most pacman and yay commands that modify the system (install, remove, update) require root privileges. You'll typically prefix them with sudo.
Placeholders: <package_name> should be replaced with the actual name of the package. [options] are optional flags.
Multiple Packages: Many commands accept multiple package names separated by spaces.
AUR Helpers: While yay is very popular, other AUR helpers exist (e.g., paru). Their syntax is often very similar to yay.
Read Prompts Carefully: Always read the output and prompts before confirming actions, especially when removing packages or upgrading.
Pacman & Yay Cheat Sheet
pacman (Official Repository Package Management)
Synchronizing Package Databases & System Updates:

sudo pacman -Sy
Synchronizes the local package databases with the repositories defined in /etc/pacman.conf. It's good practice to do this before installing or upgrading packages.
sudo pacman -Syy
Forces a refresh of all local package databases, even if they appear to be up-to-date. Use this if you suspect your local database is out of sync.
sudo pacman -Syu
Synchronizes package databases AND upgrades all currently installed packages to their newest available versions from the repositories. This is the standard command for a full system update.
sudo pacman -Syyu
Forces a database refresh and then performs a full system upgrade.
Installing Packages:

sudo pacman -S <package_name>
Installs a specific package (and its dependencies) from the repositories.
sudo pacman -S <package1_name> <package2_name>
Installs multiple packages.
sudo pacman -U /path/to/package.pkg.tar.zst (or .xz)
Installs a package from a local file (e.g., downloaded manually or from the cache). Use this if you have a .pkg.tar.zst file.
sudo pacman -S --needed <package_name>
Installs the package only if it's not already installed or if the version in the repositories is newer. Useful for scripts to avoid reinstalling.
Removing Packages:

sudo pacman -R <package_name>
Removes a specific package but leaves its dependencies installed.
sudo pacman -Rs <package_name>
Removes the package and its dependencies, provided those dependencies are not required by any other installed package and were not explicitly installed. This is generally the recommended way to remove a package and its unneeded dependencies.
sudo pacman -Rsn <package_name>
Removes the package, its unneeded dependencies (like -Rs), AND removes configuration files created by Pacman for that package (prevents .pacsave files).
sudo pacman -Rsc <package_name>
Removes the package and all packages that depend on it. Use with EXTREME CAUTION, as this can remove many essential packages if you're not careful.
sudo pacman -Rdd <package_name>
Removes a package, ignoring dependency checks. VERY DANGEROUS. Only use if you absolutely know what you are doing, as it can break your system.
Querying Packages (Searching & Getting Information):

pacman -Ss <search_term>
Searches the synchronized package databases for packages matching the search term (in names and descriptions).
pacman -Qs <search_term>
Searches for already installed packages matching the search term.
pacman -Si <package_name>
Displays detailed information about a package from the repositories (version, description, dependencies, etc.).
pacman -Qi <package_name>
Displays detailed information about an already installed package.
pacman -Ql <package_name>
Lists all files owned by an installed package.
pacman -Qo /path/to/file
Shows which installed package owns a specific file.
pacman -Q
Lists all packages installed on the system.
pacman -Qe
Lists only explicitly installed packages (those you installed directly, not dependencies).
pacman -Qd
Lists packages that were installed as dependencies but are no longer required by any explicitly installed package (orphans).
pacman -Qdt
Lists orphaned packages (similar to -Qd but often used in scripts, -t for terse output).
pacman -Qdtq
Lists orphaned packages (quiet, just names). Useful for scripting with pacman -Rns $(pacman -Qdtq).
Cleaning the System:

sudo pacman -Sc
Clears the package cache of packages that are no longer installed. It keeps cached versions of currently installed packages.
sudo pacman -Scc
Clears the entire package cache. This frees up more disk space but means if you need to reinstall or downgrade a package, it will have to be re-downloaded. Use with caution.
sudo pacman -Rns $(pacman -Qdtq)
Removes all orphaned packages (dependencies no longer needed). This is a common maintenance command.
Pacman Log:

/var/log/pacman.log
Pacman's log file, useful for reviewing installation history and troubleshooting.
yay (AUR Helper & Pacman Wrapper)
yay uses pacman for official repository operations and adds its own functionality for AUR packages. Many pacman flags work directly with yay.

Installing & Updating Packages (Official Repos & AUR):

yay <search_term> (or yay -S <search_term>)
Interactively searches for and allows you to install packages from both official repositories and the AUR. If an exact match is found for -S, it behaves like pacman -S.
yay -S <package_name>
Installs a package. If it's in the official repos, it uses pacman. If it's an AUR package, yay will handle downloading the PKGBUILD, building, and installing it.
yay -Syu
Synchronizes package databases (like pacman -Sy) AND upgrades all packages from official repositories AND the AUR. This is the recommended command for a full system update including AUR packages.
yay (with no arguments)
Alias for yay -Syu.
yay -Sua
Upgrades only AUR packages.
yay -Syyu
Forces a database refresh (like pacman -Syy) and then performs a full system and AUR upgrade.
Removing Packages (Official Repos & AUR):

yay -R <package_name>
Removes a package (same as pacman -R).
yay -Rs <package_name>
Removes a package and its unneeded dependencies (same as pacman -Rs).
yay -Rns <package_name>
Removes a package, its unneeded dependencies, and configuration files (same as pacman -Rns). Often the preferred removal command.
yay -Rsc <package_name>
Removes a package and everything that depends on it (same as pacman -Rsc). Use with EXTREME CAUTION.
Searching & Getting Information (Official Repos & AUR):

yay -Ss <search_term>
Searches for packages in both official repositories and the AUR.
yay -Si <package_name>
Shows information about a package from repos or AUR (before installation).
yay -Qi <package_name>
Shows information about an installed package (same as pacman -Qi).
yay -Ql <package_name>
Lists files owned by an installed package (same as pacman -Ql).
yay -Qo /path/to/file
Shows which installed package owns a file (same as pacman -Qo).
yay -Qm
Lists all packages installed from the AUR (or other non-official sources, i.e., "foreign" packages).
yay -Qu
Lists packages from official repositories and AUR that have updates available.
Cleaning & System Maintenance with yay:

yay -Yc
Cleans unneeded dependencies (orphans) from your system. This is a yay-specific command and is often preferred over the pacman -Rns $(pacman -Qdtq) for its interactivity and clarity.
yay -Sc
Cleans the cache of uninstalled packages (like pacman -Sc). It can also offer to clean AUR build directories.
yay -Scc
Cleans the entire pacman cache and can offer to clean all AUR build directories.
yay -Ps
Prints system statistics (package counts, disk usage, etc.).
AUR Specific yay Operations:

yay -G <aur_package_name> (or yay --getpkgbuild)
Downloads the PKGBUILD and related files for an AUR package without building or installing it. Useful for inspection or manual building.
yay -S <aur_package_name> --noconfirm
Installs an AUR package without asking for confirmation for each step (use with caution, understand what you are installing).
yay -Syu --devel
Checks for updates for -git, -svn, -hg, -bzr (VCS) packages from the AUR, which might not have a version bump but have new commits.
yay -Y --gendb
Generates a development package database for *-git packages that were installed without yay. Run once if you have such packages.
yay -Y --devel --save
Makes development package updates (checking VCS packages) permanently enabled for yay and yay -Syu.