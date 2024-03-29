PGDMP         9                |            palupi    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    115245    palupi    DATABASE     }   CREATE DATABASE palupi WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE palupi;
                postgres    false            �            1259    115262    menu    TABLE     �   CREATE TABLE public.menu (
    id_menu integer NOT NULL,
    nama character varying,
    harga money,
    kuantitas integer,
    deskripsi character varying
);
    DROP TABLE public.menu;
       public         heap    postgres    false            �            1259    115261    menu_id_menu_seq    SEQUENCE     �   ALTER TABLE public.menu ALTER COLUMN id_menu ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.menu_id_menu_seq
    START WITH 0
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            �            1259    115270 
   pembayaran    TABLE     �   CREATE TABLE public.pembayaran (
    id_pembayaran integer NOT NULL,
    id_pembeli integer,
    opsi_bayar character varying,
    total_harga money
);
    DROP TABLE public.pembayaran;
       public         heap    postgres    false            �            1259    115269    pembayaran_id_pembayaran_seq    SEQUENCE     �   ALTER TABLE public.pembayaran ALTER COLUMN id_pembayaran ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.pembayaran_id_pembayaran_seq
    START WITH 0
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            �            1259    115254 	   pemesanan    TABLE     �   CREATE TABLE public.pemesanan (
    id_pembeli integer NOT NULL,
    nama character varying,
    alamat character varying,
    telp character varying,
    pesan character varying,
    makanditempat boolean
);
    DROP TABLE public.pemesanan;
       public         heap    postgres    false            �            1259    115253    pemesanan_id_pembeli_seq    SEQUENCE     �   ALTER TABLE public.pemesanan ALTER COLUMN id_pembeli ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.pemesanan_id_pembeli_seq
    START WITH 0
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215                      0    115262    menu 
   TABLE DATA           J   COPY public.menu (id_menu, nama, harga, kuantitas, deskripsi) FROM stdin;
    public          postgres    false    217   �       	          0    115270 
   pembayaran 
   TABLE DATA           X   COPY public.pembayaran (id_pembayaran, id_pembeli, opsi_bayar, total_harga) FROM stdin;
    public          postgres    false    219                    0    115254 	   pemesanan 
   TABLE DATA           Y   COPY public.pemesanan (id_pembeli, nama, alamat, telp, pesan, makanditempat) FROM stdin;
    public          postgres    false    215                     0    0    menu_id_menu_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.menu_id_menu_seq', 0, false);
          public          postgres    false    216                       0    0    pembayaran_id_pembayaran_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.pembayaran_id_pembayaran_seq', 0, false);
          public          postgres    false    218                       0    0    pemesanan_id_pembeli_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.pemesanan_id_pembeli_seq', 0, false);
          public          postgres    false    214            r           2606    115268    menu menu_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_pkey PRIMARY KEY (id_menu);
 8   ALTER TABLE ONLY public.menu DROP CONSTRAINT menu_pkey;
       public            postgres    false    217            t           2606    115276    pembayaran pembayaran_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT pembayaran_pkey PRIMARY KEY (id_pembayaran);
 D   ALTER TABLE ONLY public.pembayaran DROP CONSTRAINT pembayaran_pkey;
       public            postgres    false    219            p           2606    115260    pemesanan pemesanan_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.pemesanan
    ADD CONSTRAINT pemesanan_pkey PRIMARY KEY (id_pembeli);
 B   ALTER TABLE ONLY public.pemesanan DROP CONSTRAINT pemesanan_pkey;
       public            postgres    false    215            u           2606    115277    pembayaran id_pembeli    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran
    ADD CONSTRAINT id_pembeli FOREIGN KEY (id_pembeli) REFERENCES public.pemesanan(id_pembeli);
 ?   ALTER TABLE ONLY public.pembayaran DROP CONSTRAINT id_pembeli;
       public          postgres    false    215    3184    219                  x������ � �      	      x������ � �            x������ � �     