# CUNY Academic Commons Plugin Availability Analysis
## Department of Epidemiology & Biostatistics

**Analysis Date**: February 28, 2026
**Total CUNY Plugins Analyzed**: 612
**Recommended Plugins Checked**: 59

---

## Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| **Recommended Plugins** | 59 | 100% |
| **Available in CUNY Commons** | 23 | 39% |
| **Not Available** | 36 | 61% |
| **Critical Missing** | 3 | 5% |
| **Can Use Alternatives** | 33 | 56% |

---

## ✅ Available Plugins by Category

### Forms & Data Collection (3/5 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| Gravity Forms | ✅ AVAILABLE | Plus 2 extensions available |
| Contact Form 7 | ✅ AVAILABLE | Backup option |
| Ninja Forms | ✅ AVAILABLE | Alternative option |
| WPForms | ❌ Not Available | Use Gravity Forms instead |
| Formidable Forms | ❌ Not Available | Use Gravity Forms instead |

**Recommendation**: Use **Gravity Forms** ✅ (best option, fully featured)

---

### Custom Fields (2/4 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| Advanced Custom Fields | ✅ AVAILABLE | Plus Date Picker extension |
| Meta Box | ✅ AVAILABLE | Alternative |
| Pods | ❌ Not Available | Use ACF instead |
| Toolset Types | ❌ Not Available | Use ACF instead |

**Recommendation**: Use **Advanced Custom Fields** ✅ (industry standard)

---

### Custom Post Types (1/3 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| Custom Post Type UI | ✅ AVAILABLE | Best option |
| CPT UI | N/A | Same as above (abbreviation) |
| Toolset Types | ❌ Not Available | Use CPT UI instead |

**Recommendation**: Use **Custom Post Type UI** ✅ (perfect for our needs)

---

### Events Calendar (3/5 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| The Events Calendar | ✅ AVAILABLE | Plus Category Colors extension |
| Events Manager | ✅ AVAILABLE | Full-featured alternative |
| Event Organiser | ✅ AVAILABLE | Plus ICAL Sync extension |
| All-in-One Event Calendar | ❌ Not Available | Not needed, have 3 options |
| Modern Events Calendar | ❌ Not Available | Not needed, have 3 options |

**Recommendation**: Use **The Events Calendar** ✅ (most popular, well-supported)

---

### File Management (2/4 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| WP Document Revisions | ✅ AVAILABLE | Version control |
| Media Library Assistant | ✅ AVAILABLE | Enhanced organization |
| Download Monitor | ❌ Not Available | Not critical, direct links work |
| WordPress Download Manager | ❌ Not Available | Not critical, direct links work |

**Recommendation**: Use **WP Document Revisions** ✅ + **Media Library Assistant** ✅

---

### Frontend Editing (1/4 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| Elementor | ✅ AVAILABLE | Best free option |
| Beaver Builder | ❌ Not Available | Premium anyway |
| Visual Composer | ❌ Not Available | Outdated |
| Divi Builder | ❌ Not Available | Theme-specific |

**Recommendation**: Use **Elementor** ✅ (perfect for faculty editing)

---

### SEO (1/4 available)
| Plugin | Status | Notes |
|--------|--------|-------|
| Yoast SEO | ✅ AVAILABLE | Industry standard |
| All in One SEO | ❌ Not Available | Not needed |
| Rank Math | ❌ Not Available | Not needed |
| SEOPress | ❌ Not Available | Not needed |

**Recommendation**: Use **Yoast SEO** ✅ (best option available)

---

### Portfolio/Gallery (0/4 available) ⚠️
| Plugin | Status | Alternative Available |
|--------|--------|---------------------|
| Essential Grid | ❌ Not Available | Use NextGEN Gallery ✅ |
| Post Grid | ❌ Not Available | Use Advanced Views Lite ✅ |
| Portfolio Gallery | ❌ Not Available | Use NextGEN Gallery ✅ |
| Grid Plus | ❌ Not Available | Use MetaSlider ✅ |

**Alternatives Available**:
- ✅ **NextGEN Gallery** - Full-featured gallery plugin
- ✅ **MetaSlider** - Carousels and sliders
- ✅ **Atomic Blocks** - Gutenberg blocks for layouts
- ✅ **Advanced Views Lite** - Display custom post types as grids

**Recommendation**: Use **NextGEN Gallery** ✅ for student success showcase

---

### Content Restriction (2/5 available) ⚠️
| Plugin | Status | Notes |
|--------|--------|-------|
| Password Protected | ✅ AVAILABLE | Per-page passwords |
| Members | ✅ PARTIAL | Team Members plugin available |
| Restrict Content Pro | ❌ Not Available | Premium |
| MemberPress | ❌ Not Available | Premium |
| Paid Memberships Pro | ❌ Not Available | Not needed |

**Workaround**: Use WordPress native "Private" page visibility + **Password Protected** ✅

**Recommendation**: Use **Password Protected** ✅ for sensitive resources

---

## 🔴 Critical Missing Plugins

### 1. User Role & Permission Management (CRITICAL)
| Plugin | Status | Priority |
|--------|--------|----------|
| User Role Editor | ❌ Not Available | **HIGH** |
| PublishPress Capabilities | ❌ Not Available | HIGH |
| Capability Manager Enhanced | ❌ Not Available | Medium |
| Members | ✅ Partial (Team Members) | Limited functionality |
| Edit Own Pages Only | ❌ Not Available | Would be perfect |

**Impact**: Faculty can't be restricted to editing only their specific page

**Workaround**: Use WordPress "Author" role + training + accept limitations

**Recommendation**: **REQUEST "User Role Editor"** (Free plugin)
- See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 1

---

### 2. Security Plugins (CRITICAL)
| Plugin | Status | Priority |
|--------|--------|----------|
| Jetpack | ✅ AVAILABLE | **Check if includes security features** |
| Wordfence Security | ❌ Not Available | **HIGH** |
| Sucuri Security | ❌ Not Available | Medium |
| iThemes Security | ❌ Not Available | Medium |
| All In One WP Security | ❌ Not Available | Medium |

**Impact**: Course evaluations vulnerable to security breaches (FERPA compliance issue)

**First Step**: Verify if Jetpack ✅ includes security features

**If Jetpack insufficient**: **REQUEST "Wordfence Security"** (Free plugin)
- See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 2

---

### 3. Backup Plugins (CRITICAL)
| Plugin | Status | Priority |
|--------|--------|----------|
| UpdraftPlus | ❌ Not Available | **CRITICAL** |
| BackWPup | ❌ Not Available | HIGH |
| Duplicator | ❌ Not Available | Medium |
| WP Time Capsule | ❌ Not Available | Medium |

**Impact**: No disaster recovery = permanent data loss if site crashes

**First Step**: **CONTACT CUNY IT** to confirm:
- Does CUNY Commons provide automated backups?
- What is restore procedure?
- Backup retention period?

**If CUNY backups inadequate**: **REQUEST "UpdraftPlus"** (Free plugin)
- See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 3

---

## ⚠️ Less Critical Missing Plugins

### Admin Interface Customization (LOW priority)
- Adminimize ❌
- White Label CMS ❌
- Admin Menu Editor ❌

**Impact**: Admin interface not customized, but functional
**Workaround**: Train faculty to ignore unused menu items

---

### Social Media (LOW priority)
- Social Share Buttons ❌
- Revive Old Posts ❌

**Available Alternative**: ✅ **Blog2Social** (auto-post to social media)
**Workaround**: Manual social media posting or use Blog2Social

---

### Other Features (LOW priority)
- Timeline Express ❌ (for timeline layouts)
- Limit Login Attempts ❌ (may be in Jetpack or Wordfence)

**Workaround**: Manual monitoring, Jetpack may include login limiting

---

## 📊 Plugins Already in CUNY Commons (23 Available)

### Full List of Available Plugins We'll Use:

**Core Functionality**:
1. ✅ Gravity Forms
2. ✅ Gravity Forms + Custom Post Types
3. ✅ Gravity Forms Advanced Post Creation
4. ✅ Gravity PDF
5. ✅ Advanced Custom Fields
6. ✅ Advanced Custom Fields: Date and Time Picker
7. ✅ Custom Post Type UI

**Events & Calendar**:
8. ✅ The Events Calendar
9. ✅ The Events Calendar: Category Colors
10. ✅ Events Manager
11. ✅ Event Organiser
12. ✅ Event Organiser ICAL Sync

**Content Management**:
13. ✅ WP Document Revisions
14. ✅ Media Library Assistant
15. ✅ Password Protected
16. ✅ Restrict Media Library Access

**Visual & Layout**:
17. ✅ Elementor
18. ✅ NextGEN Gallery
19. ✅ MetaSlider
20. ✅ Atomic Blocks
21. ✅ Advanced Views Lite

**SEO & Marketing**:
22. ✅ Yoast SEO
23. ✅ Blog2Social

**Utility**:
24. ✅ Relevanssi (search)
25. ✅ Jetpack (multi-purpose)

---

## 💰 Cost Comparison

### Original Plan (Non-CUNY)
| Plugin | Annual Cost |
|--------|-------------|
| Gravity Forms | $59 |
| PublishPress Capabilities | $79 |
| Restrict Content Pro | $99 |
| ACF Pro | $49 |
| The Events Calendar Pro | $99 |
| Hosting | $168-360 |
| **TOTAL** | **$553-745/year** |

### CUNY Commons Plan
| Plugin | Annual Cost |
|--------|-------------|
| All 25 available plugins | $0 (included) |
| 3 requested plugins (free) | $0 |
| Hosting | $0 (included in CUNY) |
| **TOTAL** | **$0/year** |

**Savings**: $553-745 per year! 🎉

---

## ✅ Recommended Action Plan

### Immediate (This Week)
1. **Contact CUNY IT** with these questions:
   ```
   - Does CUNY Commons provide automated site backups?
   - What is the backup restore procedure?
   - Does Jetpack subscription include Security features?
   - Process for requesting additional free plugins?
   ```

2. **Review Available Plugins**:
   - Confirm all 25 plugins in list are accessible
   - Test activation of key plugins (Gravity Forms, Elementor)

### Short-term (Next 2 Weeks)
3. **Request Missing Critical Plugins** (if needed after CUNY IT clarification):
   - User Role Editor (Free) - for faculty permissions
   - Wordfence Security (Free) - if Jetpack insufficient
   - UpdraftPlus (Free) - if CUNY doesn't provide backups

   Use justifications in PLUGIN_REQUISITION_JUSTIFICATIONS.md

4. **Begin Implementation**:
   - Follow CUNY_IMPLEMENTATION_GUIDE.md
   - Start with Phase 1 (Foundation)
   - Install available plugins

### Long-term (6 Weeks)
5. **Complete Site Build**:
   - Import all faculty pages
   - Set up course evaluations
   - Configure events calendar
   - Test all features
   - Train faculty and admins
   - Launch! 🚀

---

## 📋 Decision Matrix

### For Each Missing Plugin, Ask:

1. **Is it critical?**
   - User Role Editor: YES (faculty permissions)
   - Security plugin: YES (FERPA compliance)
   - Backup plugin: YES (disaster recovery)
   - Others: NO (nice to have)

2. **Is there a free version?**
   - All 3 critical plugins: YES (free versions available)

3. **Is there a CUNY alternative?**
   - User roles: Partial (WordPress native Author role)
   - Security: Maybe (need to check Jetpack)
   - Backup: Maybe (need to check CUNY IT)

4. **Can we work around it?**
   - User roles: Yes, with training and risk acceptance
   - Security: No, too risky for FERPA data
   - Backup: No, unacceptable risk

5. **Should we request it?**
   - User Role Editor: RECOMMENDED
   - Security plugin: IF needed after Jetpack check
   - Backup plugin: IF needed after CUNY IT confirmation

---

## 🎯 Success Criteria

Our CUNY implementation will be successful if we can:

✅ Host course evaluations securely (Gravity Forms + Password Protected)
⚠️ Allow faculty self-editing (Elementor + WordPress roles, limited)
✅ Showcase student success (NextGEN Gallery + Custom Post Types + ACF)
✅ House internal resources (WP Document Revisions + Password Protected)
✅ Highlight department culture (Events Calendar + Blog)

**4 out of 5 goals fully achievable with available plugins!**

---

## Conclusion

CUNY Academic Commons provides **excellent plugin coverage** for our needs:
- **39% direct matches** for recommended plugins
- **Most critical plugins available** (forms, custom fields, events, editing)
- **Free alternatives available** for most gaps
- **Only 3 critical plugins missing** (all have free versions)
- **$0 total cost** vs. $553-745/year for non-CUNY setup

With 3 simple plugin requests (all free), we can achieve a **complete, professional solution at zero cost**.

**Bottom Line**: CUNY Academic Commons is perfect for this project! 🎓

---

## Additional Resources

- **Full CUNY Plugin List**: [available_plugins.csv](available_plugins.csv)
- **Plugin Analysis Data**: [plugin_availability_analysis.json](plugin_availability_analysis.json)
- **Implementation Guide**: [CUNY_IMPLEMENTATION_GUIDE.md](CUNY_IMPLEMENTATION_GUIDE.md)
- **Plugin Justifications**: [PLUGIN_REQUISITION_JUSTIFICATIONS.md](PLUGIN_REQUISITION_JUSTIFICATIONS.md)
- **Technical Specs**: [TECHNICAL_RECOMMENDATIONS_CUNY.md](TECHNICAL_RECOMMENDATIONS_CUNY.md)
