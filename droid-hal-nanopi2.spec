# These and other macros are documented in dhd/droid-hal-device.inc
%define device nanopi2
%define vendor friendlyarm
%define vendor_pretty FriendlyARM
%define device_pretty Nano PI 2
%define installable_zip 1

%define straggler_files \
/selinux_version \
/service_contexts \
%{nil}
%include rpm/dhd/droid-hal-device.inc
