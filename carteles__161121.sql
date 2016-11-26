--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: carteles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE carteles (
    numeroserie character varying(50) NOT NULL,
    datetime character varying(30) DEFAULT 'null'::character varying NOT NULL,
    pila character varying(4) DEFAULT 'null'::character varying NOT NULL,
    temp character varying(5) DEFAULT 'null'::character varying NOT NULL,
    corriente character varying(5) DEFAULT 'null'::character varying NOT NULL,
    fuente5v boolean DEFAULT false NOT NULL,
    fuente24v boolean DEFAULT false NOT NULL,
    fuenteppic boolean DEFAULT false NOT NULL,
    fuente5pic boolean DEFAULT false NOT NULL,
    mensaje character varying(150) DEFAULT 'null'::character varying
);


ALTER TABLE carteles OWNER TO postgres;

--
-- Data for Name: carteles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY carteles (numeroserie, datetime, pila, temp, corriente, fuente5v, fuente24v, fuenteppic, fuente5pic, mensaje) FROM stdin;
00:17:4F:00:00:88	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:89	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:94	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:95	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:96	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:97	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:99	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E1	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:01	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:65	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:66	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:68	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:69	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:70	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:71	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:72	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:74	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:75	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:76	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:77	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:79	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:10	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:60	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:12	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:13	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:14	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:15	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:16	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:17	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:18	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:19	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:67	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:1F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C7	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A2	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A5	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A6	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A7	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A8	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AA	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AB	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AC	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AD	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AE	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B0	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B1	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B2	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B3	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B4	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B6	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B7	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B8	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:25	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:26	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:27	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:28	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:29	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:30	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:31	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:32	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:33	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:34	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:00	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:35	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:92	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:36	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:93	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:11	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:2E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:55	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:56	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:57	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:58	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:59	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:5F	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:61	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:62	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:63	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:64	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B9	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BA	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BC	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BD	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BE	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BF	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C1	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C2	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C3	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C4	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C6	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C8	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C9	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CA	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CB	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CD	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CE	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CF	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D0	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D1	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D3	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D4	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D5	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D6	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D7	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D9	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DA	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DB	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DC	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DE	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A4	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:02	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:03	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:04	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:05	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:06	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:07	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:08	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:09	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0A	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0B	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:0C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A0	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:91	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C5	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:CC	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D2	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:D8	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DD	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E4	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:EA	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:23	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:24	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7C	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:20	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:21	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:22	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:DF	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E0	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E2	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E3	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E5	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E6	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E7	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E8	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:E9	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:6D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:73	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:78	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:7D	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:85	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:90	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:98	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:9E	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A1	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A3	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:A9	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:AF	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:B5	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:BB	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:C0	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:80	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:81	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:82	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:83	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:84	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:86	null	null	null	null	f	f	f	f	null
00:17:4F:00:00:87	null	null	null	null	f	f	f	f	null
\.


--
-- Name: carteles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY carteles
    ADD CONSTRAINT carteles_pkey PRIMARY KEY (numeroserie);


--
-- PostgreSQL database dump complete
--

