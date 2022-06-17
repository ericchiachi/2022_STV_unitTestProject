package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }


    // ok
//    @Test
//    public void encodeBase32_withParameterLength() throws Exception {
//        // the num 753 is "rj" in encodeBase32
//            int length = 0;
//            long i = 753;
//        String encode = "";
//
//        // test length less than actually need
//        length = 1;
//        encode = Base32.encodeBase32( i, length );
//        assertEquals("rj", encode);
//
//        // test length more than actually need
//        length = 12;
//        encode = Base32.encodeBase32( i, length );
//        assertEquals("0000000000rj", encode);
//
//        // test given negative i
//        length = 1;
//        i = -i;
//        encode = Base32.encodeBase32( i, length );
//        assertEquals("-rj", encode);
//
//        // ISP
//        assertEquals("-1", Base32.encodeBase32(-1, 1));
//        assertEquals("0", Base32.encodeBase32(0, 1));
//        assertEquals("1", Base32.encodeBase32(1, 1));
//        assertEquals("1", Base32.encodeBase32(1, -1));
//        assertEquals("1", Base32.encodeBase32(1, 0));
//    }
//
//    // ok
//    @Test
//    public void encodeBase32_withoutParameterLength() throws Exception {
//        // the num 753 is "rj" in encodeBase32
//        // without input length, default is DEFULT_MAX_HASHS = 12
//        int i = 753;
//        String encode = "";
//        encode = Base32.encodeBase32( i );
//        assertEquals("0000000000rj", encode);
//
//        // ISP
//        assertEquals("-000000000001", Base32.encodeBase32(-1));
//        assertEquals("000000000000", Base32.encodeBase32(0));
//        assertEquals("000000000001", Base32.encodeBase32(1));
//
//    }
//
//    // ok
//    @Test
//    public void decodeBase32() throws Exception {
//        // the String "rj" is 753 in number
//        long i = 0;
//        long decode = 753;
//
//        // test basic decode
//        i = Base32.decodeBase32("rj");
//        assertEquals(i, decode);
//
//        // test decode with prefix "0"
//        i = Base32.decodeBase32("0000000000rj");
//        assertEquals(i, decode);
//
//        // test negative reverse
//        i = Base32.decodeBase32("-rj");
//        decode = -decode;
//        assertEquals(i, decode);
//
//        // ISP
//        String exceptionMessage = "not a base32 character: a";
//        try {
//            Base32.decodeBase32("a");
//        } catch ( IllegalArgumentException throwMessage ) {
//            assertEquals(  exceptionMessage , throwMessage.getMessage());
//        }
//    }
//
//    // ok
//    @Test
//    public void getCharIndex() throws Exception {
//        // get the index inside characters[](inside Base32.java)
//
//        char ch = '0'; // test first index
//        assertEquals( 0, Base32.getCharIndex(ch) );
//
//        ch = 'z'; // test last index
//        assertEquals( 31, Base32.getCharIndex(ch) );
//
//        ch = 'a'; // test char not in list
//        String exceptionMessage = "not a base32 character: " + ch;
//        try {
//            Base32.getCharIndex(ch);
//        } catch ( IllegalArgumentException throwMessage ) {
//            assertEquals(  exceptionMessage , throwMessage.getMessage());
//        }
//    }
//
//    // ok
//    @Test
//    public void padLeftWithZerosToLength() throws Exception {
//
//        // ISP
//        assertEquals("a", Base32.padLeftWithZerosToLength("a", 0));
//        assertEquals("a", Base32.padLeftWithZerosToLength("a", 1));
//        assertEquals("0a", Base32.padLeftWithZerosToLength("a", 2));
//
//    }

    @Test
    public void TestPadLeftWithZerosToLength() throws Exception {
        assertEquals("HelloWorld", Base32.padLeftWithZerosToLength("HelloWorld", 1));
        assertEquals("0HelloWorld", Base32.padLeftWithZerosToLength("HelloWorld", 11));
        assertEquals("00HelloWorld", Base32.padLeftWithZerosToLength("HelloWorld", 12));
    }

    @Test
    public void TestEncodeBase32() throws Exception {
        assertEquals("-1", Base32.encodeBase32(-1, 0));
        assertEquals("1", Base32.encodeBase32(1, 0));
        assertEquals("-200", Base32.encodeBase32(-2048, 0));
    }


}