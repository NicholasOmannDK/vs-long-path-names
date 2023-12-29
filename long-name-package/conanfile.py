from conans import ConanFile, CMake, tools

class LongNamePackageConan(ConanFile):
    name = "long-name-package"
    version = "0.1"
    description = "This is a package with headers with way to long of names"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="include")
        
    def package_id(self):
        self.info.header_only()