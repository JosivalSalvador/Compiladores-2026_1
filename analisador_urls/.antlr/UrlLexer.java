// Generated from /home/gaby/Documentos/Compiladores-2026_1/analisador_urls/UrlLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class UrlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, SEPARADOR=2, URL=3, DOMAIN=4, PORT=5, PATH=6, QUERY=7, FRAGMENTO=8, 
		WS=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROTOCOL", "SEPARADOR", "URL", "DOMAIN", "PORT", "PATH", "QUERY", "FRAGMENTO", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'://'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "SEPARADOR", "URL", "DOMAIN", "PORT", "PATH", "QUERY", 
			"FRAGMENTO", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public UrlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "UrlLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\t\\\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0003\u0000 \b\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002)\b\u0002\u0001\u0002\u0001\u0002\u0003\u0002-\b\u0002\u0001\u0002"+
		"\u0003\u00020\b\u0002\u0001\u0002\u0003\u00023\b\u0002\u0001\u0002\u0003"+
		"\u00026\b\u0002\u0001\u0003\u0004\u00039\b\u0003\u000b\u0003\f\u0003:"+
		"\u0001\u0004\u0001\u0004\u0004\u0004?\b\u0004\u000b\u0004\f\u0004@\u0001"+
		"\u0005\u0001\u0005\u0005\u0005E\b\u0005\n\u0005\f\u0005H\t\u0005\u0001"+
		"\u0006\u0001\u0006\u0004\u0006L\b\u0006\u000b\u0006\f\u0006M\u0001\u0007"+
		"\u0001\u0007\u0004\u0007R\b\u0007\u000b\u0007\f\u0007S\u0001\b\u0004\b"+
		"W\b\b\u000b\b\f\bX\u0001\b\u0001\b\u0000\u0000\t\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0001"+
		"\u0000\u0006\u0004\u0000-.09AZaz\u0001\u000009\u0004\u0000-9AZ__az\u0007"+
		"\u0000&&--09==AZ__az\u0005\u0000--09AZ__az\u0003\u0000\t\n\r\r  h\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0001\u001f\u0001\u0000\u0000\u0000\u0003!\u0001"+
		"\u0000\u0000\u0000\u0005(\u0001\u0000\u0000\u0000\u00078\u0001\u0000\u0000"+
		"\u0000\t<\u0001\u0000\u0000\u0000\u000bB\u0001\u0000\u0000\u0000\rI\u0001"+
		"\u0000\u0000\u0000\u000fO\u0001\u0000\u0000\u0000\u0011V\u0001\u0000\u0000"+
		"\u0000\u0013\u0014\u0005h\u0000\u0000\u0014\u0015\u0005t\u0000\u0000\u0015"+
		"\u0016\u0005t\u0000\u0000\u0016 \u0005p\u0000\u0000\u0017\u0018\u0005"+
		"h\u0000\u0000\u0018\u0019\u0005t\u0000\u0000\u0019\u001a\u0005t\u0000"+
		"\u0000\u001a\u001b\u0005p\u0000\u0000\u001b \u0005s\u0000\u0000\u001c"+
		"\u001d\u0005f\u0000\u0000\u001d\u001e\u0005t\u0000\u0000\u001e \u0005"+
		"p\u0000\u0000\u001f\u0013\u0001\u0000\u0000\u0000\u001f\u0017\u0001\u0000"+
		"\u0000\u0000\u001f\u001c\u0001\u0000\u0000\u0000 \u0002\u0001\u0000\u0000"+
		"\u0000!\"\u0005:\u0000\u0000\"#\u0005/\u0000\u0000#$\u0005/\u0000\u0000"+
		"$\u0004\u0001\u0000\u0000\u0000%&\u0003\u0001\u0000\u0000&\'\u0003\u0003"+
		"\u0001\u0000\')\u0001\u0000\u0000\u0000(%\u0001\u0000\u0000\u0000()\u0001"+
		"\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000*,\u0003\u0007\u0003\u0000"+
		"+-\u0003\t\u0004\u0000,+\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000"+
		"-/\u0001\u0000\u0000\u0000.0\u0003\u000b\u0005\u0000/.\u0001\u0000\u0000"+
		"\u0000/0\u0001\u0000\u0000\u000002\u0001\u0000\u0000\u000013\u0003\r\u0006"+
		"\u000021\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000035\u0001\u0000"+
		"\u0000\u000046\u0003\u000f\u0007\u000054\u0001\u0000\u0000\u000056\u0001"+
		"\u0000\u0000\u00006\u0006\u0001\u0000\u0000\u000079\u0007\u0000\u0000"+
		"\u000087\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:8\u0001\u0000"+
		"\u0000\u0000:;\u0001\u0000\u0000\u0000;\b\u0001\u0000\u0000\u0000<>\u0005"+
		":\u0000\u0000=?\u0007\u0001\u0000\u0000>=\u0001\u0000\u0000\u0000?@\u0001"+
		"\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000"+
		"A\n\u0001\u0000\u0000\u0000BF\u0005/\u0000\u0000CE\u0007\u0002\u0000\u0000"+
		"DC\u0001\u0000\u0000\u0000EH\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000"+
		"\u0000FG\u0001\u0000\u0000\u0000G\f\u0001\u0000\u0000\u0000HF\u0001\u0000"+
		"\u0000\u0000IK\u0005?\u0000\u0000JL\u0007\u0003\u0000\u0000KJ\u0001\u0000"+
		"\u0000\u0000LM\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001"+
		"\u0000\u0000\u0000N\u000e\u0001\u0000\u0000\u0000OQ\u0005#\u0000\u0000"+
		"PR\u0007\u0004\u0000\u0000QP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000"+
		"\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000T\u0010\u0001"+
		"\u0000\u0000\u0000UW\u0007\u0005\u0000\u0000VU\u0001\u0000\u0000\u0000"+
		"WX\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000"+
		"\u0000YZ\u0001\u0000\u0000\u0000Z[\u0006\b\u0000\u0000[\u0012\u0001\u0000"+
		"\u0000\u0000\r\u0000\u001f(,/25:@FMSX\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}