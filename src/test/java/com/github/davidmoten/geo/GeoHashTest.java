package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.*;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class GeoHashTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    // ok
//    @Test
//    public void testAdjacentHash_withoutSteps() throws Exception {
//        String hashResult = "";
//
//        // Test border situation (at the poles)
//        // The geoHash in (90, 0) is "gzzzzzzzzzzz"
//        // The "zzzzzzzzzzzb" will be the result after go Direction.TOP
//        hashResult = GeoHash.adjacentHash("gzzzzzzzzzzz", Direction.TOP );
//        assertEquals("zzzzzzzzzzzb", hashResult);
//
//        // Test border situation (at the -180,180 longitude boundaries)
//        // The geoHash in (0, 180) is "rzzzzzzzzzzz"
//        // The "2pbpbpbpbpbp" will be the result after go Direction.RIGHT
//        hashResult = GeoHash.adjacentHash("rzzzzzzzzzzz", Direction.RIGHT );
//        assertEquals("2pbpbpbpbpbp", hashResult);
//
//        // ISP
//        try {
//            hashResult = GeoHash.adjacentHash("", Direction.RIGHT );
//        } catch ( IllegalArgumentException throwMessage ) {
//            assertEquals(  "adjacent has no meaning for a zero length hash that covers the whole world" , throwMessage.getMessage());
//        }
//
//    }
//
//    // ok
//    @Test
//    public void testAdjacentHash_withSteps() throws Exception {
//
//        // positive steps value
//        String hashResult = GeoHash.adjacentHash("wsqqmx41x6fs", Direction.RIGHT, 5 );
//        assertEquals("wsqqmx41x6gu", hashResult);
//
//        // negative steps value
//        hashResult = GeoHash.adjacentHash("wsqqmx41x6fs", Direction.RIGHT, -5 );
//        assertEquals("wsqqmx41x6ck", hashResult);
//
//        // ISP
//        assertEquals("zzzzzzzzzzzb", GeoHash.adjacentHash("gzzzzzzzzzzz", Direction.TOP, 1));
//        assertEquals("2pbpbpbpbpbp", GeoHash.adjacentHash("rzzzzzzzzzzz", Direction.RIGHT, 1));
//        assertEquals("rzzzzzzzzzzz", GeoHash.adjacentHash("rzzzzzzzzzzz", Direction.RIGHT, 0));
//        assertEquals("rzzzzzzzzzzx", GeoHash.adjacentHash("rzzzzzzzzzzz", Direction.RIGHT, -1));
//
//    }
//
//    // ok
//    @Test
//    public void testRight() throws Exception {
//        assertEquals("2pbpbpbpbpbp", GeoHash.right("rzzzzzzzzzzz"));
//    }
//
//    // ok
//    @Test
//    public void testEncodeHash_latitudeAndLongitude_withoutLength() throws Exception {
//        // the GeoHash in Taipei Tech is "wsqqmx41x6fs"
//        // the (double latitude,  double longitude) in Taipei Tech is (25.043608, 121.533823)
//        String geoHash = GeoHash.encodeHash(25.043608, 121.533823);
//        assertEquals("wsqqmx41x6fs", geoHash);
//
//        // ISP
//        assertEquals("s00000000000", GeoHash.encodeHash(0.000000, 0.000000));
//        assertEquals("xbpbpbpbpbpb", GeoHash.encodeHash(0.000000, 180.000000));
//        assertEquals("800000000000", GeoHash.encodeHash(0.000000, -180.000000));
//        assertEquals("upbpbpbpbpbp", GeoHash.encodeHash(90.000000, 0.000000));
//        assertEquals("h00000000000", GeoHash.encodeHash(-90.000000, 0.000000));
//
//    }
//
//    // ok
//    @Test
//    public void testNeighbours() throws Exception {
//        // give the GeoHash in (0, 0) which is "7zzzzzzzzzzz"
//        List<String> neighbourList = GeoHash.neighbours("7zzzzzzzzzzz");
//        List<String> expectNeighborList = Arrays.asList("7zzzzzzzzzzx", "kpbpbpbpbpbp",
//                                                        "ebpbpbpbpbpb", "7zzzzzzzzzzy",
//                                                        "ebpbpbpbpbp8", "7zzzzzzzzzzw",
//                                                        "s00000000000", "kpbpbpbpbpbn");
//        for(int index=0; index<8; index++){
//            assertEquals(neighbourList.get(index), expectNeighborList.get(index));
//        }
//    }
//
//    @Test
//    public void testDecodeHash() throws Exception {
//        // the GeoHash in Taipei Tech is "wsqqmx41x6fs"
//        LatLong decode = GeoHash.decodeHash( "wsqqmx41x6fs" );
//        assertEquals( 25.043608, decode.getLat(), 0.001 );
//        assertEquals( 121.533823, decode.getLon(), 0.001 );
//    }
//
//    // ok
//    @Test
//    public void testEncodeHashToLong() throws Exception {
//        assertEquals(-4611686018427387903L, GeoHash.encodeHashToLong(0.000000, 0.000000, 1));
//        assertEquals(-1729382256910270463L, GeoHash.encodeHashToLong(0.000000, 180.000000, 1));
//        assertEquals(4611686018427387905L, GeoHash.encodeHashToLong(0.000000, -180.000000, 1));
//        assertEquals(-3458764513820540927L, GeoHash.encodeHashToLong(90.000000, 0.000000, 1));
//        assertEquals(-9223372036854775807L, GeoHash.encodeHashToLong(-90.000000, 0.000000, 1));
//        assertEquals(-4611686018427387894L, GeoHash.encodeHashToLong(0.000000, 0.000000, 10));
//
//    }
//
//    // ok
//    @Test
//    public void testFromLongtoString() throws Exception {
//        assertEquals("s", GeoHash.fromLongToString(-4611686018427387903L));
//        assertEquals("s000000000", GeoHash.fromLongToString(-4611686018427387894L));
//        try {
//            GeoHash.fromLongToString(-9223372036854775795L);
//        } catch ( IllegalArgumentException throwMessage ) {
//            assertEquals(  "invalid long geohash -9223372036854775795" , throwMessage.getMessage());
//        }
//
//    }
//
//    // ok
//    @Test
//    public void testCoverBoundingBox_withoutMaxHashes() throws Exception {
//        assertEquals("Coverage [hashes=[h, j, k, m, n, p, q, r, s, t, w, x], ratio=1.5]",
//                    GeoHash.coverBoundingBox(0.000000, 0.000000, -90.0000000, 180.000000).toString());
//        assertEquals("Coverage [hashes=[s00000000000], ratio=Infinity]",
//                    GeoHash.coverBoundingBox(0.000000, 0.000000, 0.0000000, 0.000000).toString());
//        assertEquals("Coverage [hashes=[8, 9, b, c, d, e, f, g, s, u], ratio=1.25]",
//                    GeoHash.coverBoundingBox(90.000000, -180.000000, 0.0000000, 0.000000).toString());
//        assertEquals("Coverage [hashes=[8, 9, b, c, d, e, f, g], ratio=0.9529411764705882]",
//                    GeoHash.coverBoundingBox(100.000000, -190.000000, 0.0000000, 0.000000).toString());
//
//    }
//
//    // ok
//    @Test
//    public void heightDegrees() throws Exception {
//        assertEquals(180.0, GeoHash.heightDegrees( 0 ), 0.001);
//        assertEquals(45.0, GeoHash.heightDegrees( 1 ), 0.001);
//        assertEquals(1.6763806343078613E-7, GeoHash.heightDegrees( 12 ), 0.001);
//        assertEquals(4.190951585769653E-8, GeoHash.heightDegrees( 13 ), 0.001);
//    }
//
//    // ok
//    @Test
//    public void widthDegrees() throws Exception {
//        assertEquals(360.0, GeoHash.widthDegrees( 0 ), 0.001);
//        assertEquals(45.0, GeoHash.widthDegrees( 1 ), 0.001);
//        assertEquals(3.3527612686157227E-7, GeoHash.widthDegrees( 12 ), 0.001);
//        assertEquals(4.190951585769653E-8, GeoHash.widthDegrees( 13 ), 0.001);
//    }


    @Test
    public void TestAdjacentHash() throws Exception {
        try {
            GeoHash.adjacentHash(null, Direction.TOP);
        } catch ( IllegalArgumentException throwMessage ) {
            assertEquals(  "hash must be non-null" , throwMessage.getMessage());
        }

        try {
            GeoHash.adjacentHash("", Direction.TOP);
        } catch ( IllegalArgumentException throwMessage ) {
            assertEquals(  "adjacent has no meaning for a zero length hash that covers the whole world" , throwMessage.getMessage());
        }
        assertEquals("y", GeoHash.adjacentHash("w", Direction.TOP));
        assertEquals("wt", GeoHash.adjacentHash("ws", Direction.TOP));
        assertEquals("wsw", GeoHash.adjacentHash("wsq", Direction.TOP));
        assertEquals("zzzzzzzzzzzb", GeoHash.adjacentHash("gzzzzzzzzzzz", Direction.TOP));

    }

    @Test
    public void TestGridToString() throws Exception {
        Set<String> hashes = new HashSet<String>();
        hashes.add("f2");
        hashes.add("f8");
        assertEquals("", GeoHash.gridAsString("dr",1,1,-1,-1, hashes));
        assertEquals("\n", GeoHash.gridAsString("dr",1,1,-1,1, hashes));
        assertEquals("dw \n", GeoHash.gridAsString("dr",1,1,1,1, hashes));

        hashes = new HashSet<String>();
        hashes.add("dw");
        assertEquals("DW \n", GeoHash.gridAsString("dr",1,1,1,1, hashes));

        hashes = new HashSet<String>();
        hashes.add("he");
        hashes.add("we");
        assertEquals("dq dw \n", GeoHash.gridAsString("dr",0,1,1,1, hashes));
        assertEquals("dx \ndw \n", GeoHash.gridAsString("dr",1,0,1,1, hashes));
    }

    @Test
    public void TestCalculateWidthDegrees() throws Exception {
        assertEquals(1.0231815394945443E-11, GeoHash.widthDegrees(18), 0.001);
        assertEquals(1.2789769243681803E-12, GeoHash.widthDegrees(19), 0.001);
    }

    @Test
    public void TestCoverBoundingBoxMaxHashes() throws Exception {
        Coverage coverage = null;
        coverage = GeoHash.coverBoundingBoxMaxHashes(1,0,0,1,5);
        assertEquals("[s00]", coverage.getHashes().toString());

        coverage = GeoHash.coverBoundingBoxMaxHashes(0,0,0,0,4);
        assertEquals("[s00000000000]", coverage.getHashes().toString());
    }


}