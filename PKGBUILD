_gitname=wiggle
pkgname=wiggle-git
pkgver=r1.14be971
pkgrel=1
pkgdesc="A python script that allows you to wiggle."
arch=('any')
url="https://github.com/FjorgeTheHuman/wiggle"
license=('GPL3')
depends=('python')
makedepends=('git')
provides=('wiggle')
source=("git+https://github.com/FjorgeTheHuman/$_gitname.git")
md5sums=('SKIP')

pkgver() {
  cd "$_gitname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    # Run the install
    cd "${srcdir}/$_gitname"
    DESTDIR="$pkgdir" make install

    # Have to redirect the prefix to arch's default location
    cd "$pkgdir"/usr/bin
    sed "$_gitname" -i -e "s:^PREFIX=.*:PREFIX=/usr/share/$_gitname:g"
}
