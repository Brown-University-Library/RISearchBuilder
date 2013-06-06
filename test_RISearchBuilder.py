import unittest
from riSearchBuilder import RISearchBuilder, RITriple


class RISearchBuilderTest( unittest.TestCase ):

    def test_using_string(self):
        ri = RISearchBuilder()
        ri.and_clause( "$item <fedora-rels-ext:%s> <info:fedora/%s>" % ("isMemberOf", "bdr:2559") )
        ri.and_clause( "$item <bul-rel:hasPagination> $page" ).order_by("$page")
        self.assertEqual(
            ri.serialize(joiner=' '),
            'select $page $item from <#ri> where $item <fedora-rels-ext:isMemberOf> <info:fedora/bdr:2559> and $item <bul-rel:hasPagination> $page order by $page'
            )
        self.assertEqual(
            type( ri.serialize(joiner=' ') ),
            str  # not unicode?  :)
            )

    def test_using_ritriple(self):
        ri2 = RISearchBuilder()
        ri2.and_clause( RITriple( "$item", "<fedora-rels-ext:%s>" % "isAnnotationOf", "<info:fedora/%s>" % "bdr:11111") )
        ri2.and_clause( "$item <bul-rel:hasPagination> $page" ).order_by("$monkey")
        self.assertEqual(
            ri2.serialize(joiner="\n"),
            'select $page $item\nfrom <#ri>\nwhere\n$item <fedora-rels-ext:isAnnotationOf> <info:fedora/bdr:11111> and $item <bul-rel:hasPagination> $page'
            )

    def test_passing_in_ritriple(self):
        myClause = RITriple("$item", "<fedora-rels-ext:%s>" % "isMemberOf", "<info:fedora/%s>" % "bdr:2222")
        ri3 = RISearchBuilder( [myClause] ).order_by("$item")
        self.assertEqual(
            ri3.serialize("\n"),
            'select $item\nfrom <#ri>\nwhere\n$item <fedora-rels-ext:isMemberOf> <info:fedora/bdr:2222>\norder by $item'
            )


if __name__ == "__main__":
  unittest.main()
