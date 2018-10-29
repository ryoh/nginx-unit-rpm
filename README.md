# nginx-unit.spec
nginx unit spec file. https://github.com/nginx/unit

# Usage

```bash
git clone nginx-unit.spec
cd nginx-unit.spec
bash ./prepare.sh
```

# Build

```bash
rpmbuild -ba SPEC/unit.spec
```

# Install 

```bash
yum install RPMS/x86_64/unit-VERSION.el7.x86_64.rpm
```

# ChangeLog
- Mon Oct 29: Change bump up version unit: 1.4 -> 1.5
