# Generated by Django 2.2.3 on 2020-01-15 11:59

from django.conf import settings
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import master.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agama', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Agama')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Agama',
                'verbose_name_plural': 'Agama',
            },
        ),
        migrations.CreateModel(
            name='Berkas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Archive'), (3, 'Draft')], db_index=True, default=6, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(editable=False, null=True)),
                ('verified_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('rejected_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nama_berkas', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Nama Berkas')),
                ('berkas', master.models.FileField(max_length=255, upload_to=master.models.PathAndRename('berkas/'))),
                ('no_berkas', models.CharField(blank=True, db_index=True, help_text='Masukkan Nomor Surat / Berkas jika ada.', max_length=30, null=True, verbose_name='Nomor Berkas')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Berkas',
                'verbose_name_plural': 'Berkas',
            },
        ),
        migrations.CreateModel(
            name='Desa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Kode')),
                ('nama_desa', models.CharField(db_index=True, max_length=40, null=True, verbose_name='Nama Desa / Kelurahan')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('lt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitute')),
                ('lg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitute')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Desa / Kelurahan',
                'verbose_name_plural': 'Desa / Kelurahan',
                'ordering': ['nama_desa'],
            },
        ),
        migrations.CreateModel(
            name='JenisKelamin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kelamin', models.CharField(db_index=True, max_length=100, verbose_name='Jenis Kelamin')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Jenis Kelamin',
                'verbose_name_plural': 'Jenis Kelamin',
            },
        ),
        migrations.CreateModel(
            name='JenisNomorIdentitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_nomor_identitas', models.CharField(max_length=30, verbose_name='Jenis Nomor Identitas')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True)),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Jenis Nomor Identitas',
                'verbose_name_plural': 'Jenis Nomor Identitas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, db_index=True, max_length=6, null=True, verbose_name='Kode')),
                ('nama_kabupaten', models.CharField(max_length=40, verbose_name='Kabupaten / Kota')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('lt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitute')),
                ('lg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitute')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kabupaten / Kota',
                'verbose_name_plural': 'Kabupaten / Kota',
                'ordering': ['nama_kabupaten'],
            },
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, db_index=True, max_length=6, null=True, verbose_name='Kode')),
                ('nama_kecamatan', models.CharField(max_length=40, verbose_name='Kecamatan')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('lt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitute')),
                ('lg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitute')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kecamatan',
                'verbose_name_plural': 'Kecamatan',
                'ordering': ['nama_kecamatan'],
            },
        ),
        migrations.CreateModel(
            name='Negara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_negara', models.CharField(db_index=True, max_length=40, verbose_name='Negara')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Kode Negara')),
                ('lt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitute')),
                ('lg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitute')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Negara',
                'verbose_name_plural': 'Negara',
                'ordering': ['nama_negara'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100, verbose_name='Nama Parameter')),
                ('value', models.CharField(max_length=100, verbose_name='Nilai')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Setting',
            },
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, db_index=True, max_length=6, null=True, verbose_name='Kode')),
                ('nama_provinsi', models.CharField(max_length=40, verbose_name='Provinsi')),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keterangan')),
                ('lt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitute')),
                ('lg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitute')),
                ('sv', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('negara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Negara', verbose_name='Negara')),
            ],
            options={
                'verbose_name': 'Provinsi',
                'verbose_name_plural': 'Provinsi',
                'ordering': ['nama_provinsi'],
            },
        ),
        migrations.AddIndex(
            model_name='negara',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_nega_sv_e07ee9_gin'),
        ),
        migrations.AddField(
            model_name='kecamatan',
            name='kabupaten',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Kabupaten', verbose_name='Kabupaten / Kota'),
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Provinsi', verbose_name='Provinsi'),
        ),
        migrations.AddIndex(
            model_name='jenisnomoridentitas',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_jeni_sv_fad733_gin'),
        ),
        migrations.AddIndex(
            model_name='jeniskelamin',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_jeni_sv_56095f_gin'),
        ),
        migrations.AddField(
            model_name='desa',
            name='kecamatan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Kecamatan', verbose_name='Kecamatan'),
        ),
        migrations.AddField(
            model_name='berkas',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_berkas_create_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Dibuat Oleh'),
        ),
        migrations.AddField(
            model_name='berkas',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_berkas_rejected_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Dibatalkan Oleh'),
        ),
        migrations.AddField(
            model_name='berkas',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_berkas_verify_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Diverifikasi Oleh'),
        ),
        migrations.AddIndex(
            model_name='agama',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_agam_sv_4fbe83_gin'),
        ),
        migrations.AddIndex(
            model_name='provinsi',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_prov_sv_4f2c01_gin'),
        ),
        migrations.AddIndex(
            model_name='kecamatan',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_keca_sv_9dc0c5_gin'),
        ),
        migrations.AddIndex(
            model_name='kabupaten',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_kabu_sv_c028e8_gin'),
        ),
        migrations.AddIndex(
            model_name='desa',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_desa_sv_509de1_gin'),
        ),
        migrations.AddIndex(
            model_name='berkas',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='master_berk_sv_5c0660_gin'),
        ),
    ]
