cd $PREFIX/lib/metasploit-framework
gem sources --add https://mirrors.njupt.edu.cn/nexus/repository/rubygems/ --remove https://rubygems.org/
gem install bundler
sed 's|nokogiri (1.*)|nokogiri (1.8.0)|g' -i Gemfile.lock
gem install nokogiri -v 1.8.0 -- --use-system-libraries
gem install actionpack
bundle update activesupport
bundle update --bundler
bundle install -j$(nproc --all)
