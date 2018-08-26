from conans import ConanFile, AutoToolsBuildEnvironment


class LibevConan(ConanFile):
    name = "libev"
    version = "4.24"
    license = "http://cvs.schmorp.de/libev/LICENSE?view=markup"
    url = "http://software.schmorp.de/pkg/libev.html"
    description = "A full-featured and high-performance event loop that is loosely modelled after libevent, but without its limitations and bugs."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = ["FindLibev.cmake"]

    def source(self):
        self.run("wget http://dist.schmorp.de/libev/libev-4.24.tar.gz")
        self.run("tar xf libev-4.24.tar.gz")


    def build(self):
        self.autotools = AutoToolsBuildEnvironment(self)
        self.autotools.configure(configure_dir="libev-4.24")
        self.autotools.make()


    def package(self):
        self.autotools.install()
        self.copy("FindLibev.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.libs = ["ev"]


